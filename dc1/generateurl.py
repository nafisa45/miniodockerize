from minio import Minio
from minio.error import S3Error
from datetime import timedelta, datetime

# In-memory storage for URLs and their expiration times
url_store = {}

def create_client():
    return Minio(
        "localhost:9000",
        access_key="A1GL9T1LKJXPS69ZVJ91",
        secret_key="53A9ySnmg6dWOpCbzc2Ssn6YTlyS8q3Jzz+f9aPv",
        secure=False
    )

def check_and_create_bucket(client, bucket_name):
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

def check_and_upload_image(client, bucket_name, source_file, destination_file):
    try:
        # Check if the object exists
        client.stat_object(bucket_name, destination_file)
        print("Object", destination_file, "already exists in bucket", bucket_name)
    except S3Error as err:
        if err.code == "NoSuchKey":
            # Upload the image if it does not exist
            client.fput_object(bucket_name, destination_file, source_file)
            print(
                source_file, "successfully uploaded as object",
                destination_file, "to bucket", bucket_name,
            )
        else:
            raise

def generate_presigned_url(client, bucket_name, object_name, expires_days):
    # Generate a pre-signed URL
    url = client.get_presigned_url(
        "GET", bucket_name, object_name, expires=timedelta(days=expires_days)
    )
    expiration_time = datetime.now() + timedelta(days=expires_days)
    return url, expiration_time

def get_presigned_url(bucket_name, object_name, expires_days):
    client = create_client()
    check_and_create_bucket(client, bucket_name)
    check_and_upload_image(client, bucket_name, object_name, object_name)
    
    # Check if URL exists and if it's still valid
    if object_name in url_store:
        url, expiration_time = url_store[object_name]
        if expiration_time > datetime.now():
            print("Existing URL is still valid.")
            return url

    # Generate a new URL if it doesn't exist or has expired
    url, expiration_time = generate_presigned_url(client, bucket_name, object_name, expires_days)
    url_store[object_name] = (url, expiration_time)
    print("Generated new URL.")
    return url

# Example usage
bucket_name = "python-test-bucket"
object_name = "flower.jpeg"
expires_days = 7  # Set the expiration time as needed

try:
    url = get_presigned_url(bucket_name, object_name, expires_days)
    print("Image URL:", url)
except S3Error as exc:
    print("Error occurred:", exc)
