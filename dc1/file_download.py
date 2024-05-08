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

    # The source bucket and filename on the MinIO server
    bucket_name = "python-test-bucket"
    source_file = "my-test-file.txt"
    
    # The path to download the file locally
    download_path = "/home/hp/dc/temp/my-downloaded-file.txt"
    
    # Download the file from MinIO bucket
    try:
        client.fget_object(bucket_name, source_file, download_path)
        print("File", source_file, "successfully downloaded to", download_path)
    except S3Error as exc:
        print("Error occurred while downloading the file:", exc)

if __name__ == "__main__":
    main()
