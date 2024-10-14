# List Running EC2 Instances
# Problem: Write a script to list all running EC2 instances.
# Objective: Practice EC2 instance management.

# list_running_ec2_instances.py
import boto3

def list_running_instances():
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    # Filter for instances that are running
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # Retrieve running instances
    instances = ec2.describe_instances(Filters=filters)

    # Print details of each running instance
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_id = instance['InstanceId']
            instance_type = instance['InstanceType']
            launch_time = instance['LaunchTime']
            public_ip = instance.get('PublicIpAddress', 'No Public IP')
            print(f"Instance ID: {instance_id}, Type: {instance_type}, Launch Time: {launch_time}, Public IP: {public_ip}")

if __name__ == "__main__":
    list_running_instances()
