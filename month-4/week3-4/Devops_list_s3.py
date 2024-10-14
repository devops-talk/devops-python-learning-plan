# List All S3 Buckets
# Problem: Implement a script to list all S3 buckets in your AWS account.
# Objective: Learn to interact with S3 using Boto3.


# list_s3_buckets.py
import boto3

# Initialize a session using Boto3
s3 = boto3.client('s3')

def list_buckets():
    # Fetch the list of all buckets
    response = s3.list_buckets()

    # Print out the bucket names
    print("Existing buckets:")
    for bucket in response['Buckets']:
        print(f"  {bucket['Name']}")

if __name__ == "__main__":
    list_buckets()
