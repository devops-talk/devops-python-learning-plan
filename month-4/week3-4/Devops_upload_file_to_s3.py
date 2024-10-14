# Upload a File to S3
# Problem: Write a script to upload a file to a specified S3 bucket.
# Objective: Practice file handling and S3 integration.


# upload_to_s3.py
import boto3
from botocore.exceptions import NoCredentialsError

def upload_file_to_s3(file_name, bucket_name, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Initialize an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file to S3 bucket
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'")
    except FileNotFoundError:
        print(f"The file {file_name} was not found")
    except NoCredentialsError:
        print("Credentials not available")

if __name__ == "__main__":
    # Specify your file name and S3 bucket name
    file_name = 'example.txt'   # Replace with your file path
    bucket_name = 'my-bucket'   # Replace with your S3 bucket name

    upload_file_to_s3(file_name, bucket_name)
