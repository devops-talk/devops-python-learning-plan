# AWS Resource Management (Class-Based)
# Problem: Create a class AWSResourceManager that has methods to:
# start_instance()
# stop_instance()
# list_resources()
# Simulate managing mock AWS resources.
# Objective: Use OOP principles to simulate AWS resource management, which is relevant to DevOps tasks.
# AWSResourceManager class to simulate AWS resource management


class AWSResourceManager:
    def __init__(self):
        self.resources = {
            'i-12345': 'stopped',
            'i-67890': 'running',
            'i-54321': 'stopped'
        }

    def start_instance(self, instance_id):
        if instance_id in self.resources:
            if self.resources[instance_id]=='stopped':
                self.resources[instance_id] = 'running'
                print(f"Instance {instance_id} started.")
            else:
                print(f"Instance {instance_id} is already running.")

    def stop_instance(self, instance_id):
        if instance_id in self.resources:
            if self.resources[instance_id] == 'running':
                self.resources[instance_id] = 'stopped'
                print(f"Instance {instance_id} stopped.")
            else:
                print(f"Instance {instance_id} is already stopped.")
        else:
            print(f"Instance {instance_id} not found.")

    def list_resources(self):
        print("Listing all resources:")
        for instance_id, status in self.resources.items():
            print(f"Instance ID: {instance_id}, Status: {status}")

aws_manager = AWSResourceManager()


aws_manager.list_resources()


aws_manager.start_instance('i-12345') 
aws_manager.stop_instance('i-67890')   


aws_manager.list_resources()