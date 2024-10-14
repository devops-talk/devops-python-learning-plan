# Manage IAM Roles
# Problem: Write a script to create, attach, and delete IAM roles for an EC2 instance.
# Objective: Automate IAM role assignments.


# manage_iam_roles.py
import boto3
import json
import time

def create_iam_role(role_name, trust_policy):
    iam = boto3.client('iam')

    try:
        response = iam.create_role(
            RoleName=role_name,
            AssumeRolePolicyDocument=json.dumps(trust_policy)
        )
        print(f"Successfully created role: {role_name}")
        return response['Role']['Arn']

    except iam.exceptions.EntityAlreadyExistsException:
        print(f"Role {role_name} already exists.")
        return iam.get_role(RoleName=role_name)['Role']['Arn']
    except Exception as e:
        print(f"Error creating role: {e}")
        return None

def attach_role_to_instance(instance_id, role_name):
    ec2 = boto3.client('ec2')

    try:
        response = ec2.associate_iam_instance_profile(
            IamInstanceProfile={
                'Name': role_name
            },
            InstanceId=instance_id
        )
        print(f"Successfully attached role {role_name} to instance {instance_id}")
    except Exception as e:
        print(f"Error attaching role: {e}")

def delete_iam_role(role_name):
    iam = boto3.client('iam')

    try:
        # Detach all policies from the role first
        attached_policies = iam.list_attached_role_policies(RoleName=role_name)['AttachedPolicies']
        for policy in attached_policies:
            iam.detach_role_policy(RoleName=role_name, PolicyArn=policy['PolicyArn'])

        # Delete the role
        iam.delete_role(RoleName=role_name)
        print(f"Successfully deleted role: {role_name}")
    except Exception as e:
        print(f"Error deleting role: {e}")

if __name__ == "__main__":
    role_name = input("Enter the IAM role name: ")

    # Trust policy that allows EC2 to assume the role
    trust_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Service": "ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    }

    instance_id = input("Enter the EC2 instance ID to attach the role: ")

    # Create IAM role
    role_arn = create_iam_role(role_name, trust_policy)

    if role_arn:
        # Attach the IAM role to the EC2 instance
        attach_role_to_instance(instance_id, role_name)

        # Wait for a few seconds to allow the role to be attached
        time.sleep(10)

        # Optionally, delete the role after attaching
        delete_confirmation = input("Do you want to delete the IAM role? (yes/no): ")
        if delete_confirmation.lower() == 'yes':
            delete_iam_role(role_name)
