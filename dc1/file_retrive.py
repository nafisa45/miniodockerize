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

    # The destination bucket and filename on the MinIO server
    bucket_name = "python-test-bucket"
    destination_file = "my-test-file.txt"
    
    # Download the file from MinIO
    try:
        data = client.get_object(bucket_name, destination_file)
        # Read and print the content of the file
        content = data.read()
        print("Content of", destination_file, ":", content.decode())
    except S3Error as exc:
        print("Error occurred while retrieving the file:", exc)

if __name__ == "__main__":
    main()
