# Launch EC2 Instance with User Data
# Problem: Write a Boto3 script to launch an EC2 instance with user data (to run a startup script).
# Objective: Automate EC2 instance initialization.
# launch_ec2_instance.py
import boto3

def launch_ec2_instance(image_id, instance_type, key_name, user_data, security_group_ids):
    ec2 = boto3.client('ec2')

    try:
        response = ec2.run_instances(
            ImageId=image_id,
            InstanceType=instance_type,
            KeyName=key_name,
            UserData=user_data,
            MinCount=1,
            MaxCount=1,
            SecurityGroupIds=security_group_ids,
        )

        instance_id = response['Instances'][0]['InstanceId']
        print(f"Successfully launched EC2 instance: {instance_id}")

    except Exception as e:
        print(f"Error launching EC2 instance: {e}")

if __name__ == "__main__":
    # Replace the following variables with your values
    image_id = input("Enter the AMI ID (e.g., ami-12345678): ")
    instance_type = input("Enter the instance type (e.g., t2.micro): ")
    key_name = input("Enter the key pair name: ")
    security_group_ids = input("Enter the security group IDs (comma-separated): ").split(',')

    # Sample user data script to install Apache web server
    user_data = '''#!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    echo "<h1>Hello from EC2!</h1>" > /var/www/html/index.html
    '''

    launch_ec2_instance(image_id, instance_type, key_name, user_data, security_group_ids)
