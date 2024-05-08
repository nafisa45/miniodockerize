from minio import Minio
from minio.error import S3Error

def main():
    # Create a client with the MinIO server configured in Docker Compose
    client = Minio(
        "localhost:9000",
        access_key="9LF6M9FLJZY3D18BMB4R",
        secret_key="CsWxaLoAsNenr11QLWM+PZEIMJf9kb4LteeGOpX8",
        secure=False
    )

    # The file to upload, change this path if needed
    source_file = "test-file.txt"
    source_file_1 = "flower.jpeg"

    # The destination bucket and filename on the MinIO server
    bucket_name = "python-test-bucket"
    destination_file = "my-test-file.txt"
    destination_file_1= "my-test-file1.txt"
    
    # Make the bucket if it doesn't exist.
    found = client.bucket_exists(bucket_name)
    if not found:
        client.make_bucket(bucket_name)
        print("Created bucket", bucket_name)
    else:
        print("Bucket", bucket_name, "already exists")

    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file, source_file,
    )
    print(
        source_file, "successfully uploaded as object",
        destination_file, "to bucket", bucket_name,
    )
    # Upload the file, renaming it in the process
    client.fput_object(
        bucket_name, destination_file_1, source_file_1,
    )
    print(
        source_file_1, "successfully uploaded a image as object",
        destination_file_1, "to bucket", bucket_name,
    )

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("Error occurred:", exc)
