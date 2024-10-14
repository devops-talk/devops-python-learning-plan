# Create an S3 Bucket
# Problem: Write a Boto3 script to create a new S3 bucket.
# Objective: Understand bucket creation and permissions.

# create_s3_bucket.py
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region=None):
    try:
        # Create the S3 client
        s3_client = boto3.client('s3', region_name=region)
        
        # Create the S3 bucket
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={
                    'LocationConstraint': region
                }
            )
        print(f"Bucket '{bucket_name}' created successfully.")
    except ClientError as e:
        print(f"Error: {e}")
        return False
    return True

if __name__ == "__main__":
    # Replace with your desired bucket name and region
    bucket_name = 'my-unique-bucket-name'  # Bucket name must be unique across all S3 users
    region = 'us-west-1'  # Replace with your preferred AWS region

    create_bucket(bucket_name, region)
