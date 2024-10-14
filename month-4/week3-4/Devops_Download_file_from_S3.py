# Download a File from S3
# Problem: Write a script to download a file from an S3 bucket.
# Objective: Automate S3 file operations.


# download_from_s3.py
import boto3
from botocore.exceptions import NoCredentialsError

def download_file_from_s3(bucket_name, object_name, file_name=None):
    # If local file_name was not specified, use object_name
    if file_name is None:
        file_name = object_name

    # Initialize an S3 client
    s3_client = boto3.client('s3')

    try:
        # Download the file from S3 bucket
        s3_client.download_file(bucket_name, object_name, file_name)
        print(f"File '{object_name}' downloaded successfully from bucket '{bucket_name}' to '{file_name}'")
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found")
    except NoCredentialsError:
        print("Credentials not available")

if __name__ == "__main__":
    # Specify the S3 bucket name and object key
    bucket_name = 'my-bucket'    # Replace with your S3 bucket name
    object_name = 'example.txt'  # Replace with your S3 object key
    file_name = 'downloaded_example.txt'  # Replace with your desired local file name

    download_file_from_s3(bucket_name, object_name, file_name)
