# Delete an RDS Instance
# Problem: Write a script to delete an RDS instance.
# Objective: Clean up RDS instances programmatically.


# delete_rds_instance.py
import boto3

def delete_rds_instance(instance_identifier, skip_final_snapshot=True):
    # Create an RDS client
    rds = boto3.client('rds')

    try:
        # Delete the RDS instance
        response = rds.delete_db_instance(
            DBInstanceIdentifier=instance_identifier,
            SkipFinalSnapshot=skip_final_snapshot  # Set to False if you want to create a final snapshot
        )

        print(f"RDS instance deletion initiated: {instance_identifier}")
        print("Response:", response)

    except Exception as e:
        print(f"Error deleting RDS instance {instance_identifier}: {e}")

if __name__ == "__main__":
    # Specify the DB instance identifier to delete
    instance_identifier = input("Enter the DB Instance Identifier to delete: ")
    
    # Option to create a final snapshot before deletion
    skip_final_snapshot = input("Skip final snapshot? (yes/no): ").strip().lower() == "yes"

    delete_rds_instance(instance_identifier, skip_final_snapshot)
