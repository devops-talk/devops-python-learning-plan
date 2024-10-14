# Start and Stop EC2 Instances
# Problem: Write a script to start and stop an EC2 instance using Boto3.
# Objective: Practice controlling EC2 instances programmatically.


import boto3

# Function to start an EC2 instance
def start_instance(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.start_instances(InstanceIds=[instance_id])
    print(f'Starting EC2 instance: {instance_id}')
    return response

# Function to stop an EC2 instance
def stop_instance(instance_id, region='us-east-1'):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopping EC2 instance: {instance_id}')
    return response

# Example usage
if __name__ == "__main__":
    instance_id = 'i-1234567890abcdef0'  # Replace with your EC2 instance ID
    region = 'us-east-1'  # Replace with your desired AWS region

    action = input("Enter 'start' to start the instance or 'stop' to stop it: ").strip().lower()

    if action == 'start':
        start_instance(instance_id, region)
    elif action == 'stop':
        stop_instance(instance_id, region)
    else:
        print("Invalid action. Please enter 'start' or 'stop'.")
