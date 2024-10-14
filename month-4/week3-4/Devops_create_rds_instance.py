# Create an RDS Instance
# Problem: Write a script to create an RDS instance using Boto3.
# Objective: Automate database management.

# create_rds_instance.py
import boto3

def create_rds_instance(instance_identifier, db_instance_class, engine, master_username, master_password):
    # Create an RDS client
    rds = boto3.client('rds')

    try:
        # Create the RDS instance
        response = rds.create_db_instance(
            DBInstanceIdentifier=instance_identifier,
            DBInstanceClass=db_instance_class,
            Engine=engine,
            MasterUsername=master_username,
            MasterUserPassword=master_password,
            AllocatedStorage=20,  # Adjust storage as needed
            StorageType='gp2',    # General Purpose SSD
            BackupRetentionPeriod=7,  # Days to retain backups
            VpcSecurityGroupIds=[]  # Specify your VPC security group IDs if needed
        )

        print(f"RDS instance creation initiated: {instance_identifier}")
        print("Response:", response)

    except Exception as e:
        print(f"Error creating RDS instance {instance_identifier}: {e}")

if __name__ == "__main__":
    # Specify the parameters for the RDS instance
    instance_identifier = input("Enter the DB Instance Identifier: ")
    db_instance_class = input("Enter the DB Instance Class (e.g., db.t2.micro): ")
    engine = input("Enter the Database Engine (e.g., mysql, postgres): ")
    master_username = input("Enter the Master Username: ")
    master_password = input("Enter the Master Password: ")

    create_rds_instance(instance_identifier, db_instance_class, engine, master_username, master_password)
