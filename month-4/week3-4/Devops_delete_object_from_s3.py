# Delete Objects from S3 Bucket
# Problem: Write a script to delete all objects in a specific S3 bucket.
# Objective: Automate S3 resource management.

# delete_s3_objects.py
import boto3

def delete_objects_from_s3_bucket(bucket_name):
    s3 = boto3.client('s3')

    # List all objects in the specified bucket
    try:
        objects_to_delete = s3.list_objects_v2(Bucket=bucket_name)
        if 'Contents' not in objects_to_delete:
            print(f"No objects found in bucket: {bucket_name}")
            return

        delete_us = {'Objects': []}

        # Collect all objects for deletion
        for obj in objects_to_delete['Contents']:
            delete_us['Objects'].append({'Key': obj['Key']})

        # Delete objects in the bucket
        if delete_us['Objects']:
            response = s3.delete_objects(Bucket=bucket_name, Delete=delete_us)
            deleted = response.get('Deleted', [])
            print(f"Deleted {len(deleted)} objects from bucket: {bucket_name}")
        else:
            print(f"No objects to delete in bucket: {bucket_name}")

    except Exception as e:
        print(f"Error deleting objects: {e}")

if __name__ == "__main__":
    bucket_name = input("Enter the S3 bucket name: ")
    delete_objects_from_s3_bucket(bucket_name)
