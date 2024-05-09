from minio import Minio
from minio.error import S3Error
from datetime import timedelta

def main():
    # Create a client with the MinIO server configured in Docker Compose
    client = Minio(
        "localhost:9000",
        access_key="9LF6M9FLJZY3D18BMB4R",
        secret_key="CsWxaLoAsNenr11QLWM+PZEIMJf9kb4LteeGOpX8",
        secure=False
    )

    # The image file to upload
    source_file = "flower.jpeg"

    # The destination bucket and filename on the MinIO server
    bucket_name = "python-test-bucket"
    destination_file = "flower.jpeg"
    
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the image
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )
    
    # Get URL for the image with 3 months expiration
    image_url = client.get_presigned_url("GET", bucket_name, destination_file, expires=timedelta(days=7))
    print("Image URL:", image_url)

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("Error occurred:", exc)
