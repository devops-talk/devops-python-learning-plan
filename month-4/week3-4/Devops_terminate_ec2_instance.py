# Terminate an EC2 Instance
# Problem: Implement a script to terminate an EC2 instance by instance ID.
# Objective: Automate resource cleanup.

# terminate_ec2_instance.py
import boto3

def terminate_instance(instance_id):
    # Create an EC2 client
    ec2 = boto3.client('ec2')

    try:
        # Terminate the specified EC2 instance
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Termination initiated for instance ID: {instance_id}")

        # Print the response from the terminate_instances call
        for instance in response['TerminatingInstances']:
            print(f"Instance ID: {instance['InstanceId']}, State: {instance['CurrentState']['Name']}")
    except Exception as e:
        print(f"Error terminating instance {instance_id}: {e}")

if __name__ == "__main__":
    # Specify the instance ID to terminate
    instance_id = input("Enter the Instance ID to terminate: ")
    terminate_instance(instance_id)
