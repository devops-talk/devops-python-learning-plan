# Send Message to SQS Queue
# Problem: Implement a script to send a message to an AWS SQS queue.
# Objective: Learn about messaging services with SQS.

# send_sqs_message.py
import boto3

def send_message_to_sqs(queue_url, message_body):
    # Create an SQS client
    sqs = boto3.client('sqs')

    try:
        # Send a message to the SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )

        print(f"Message sent to SQS queue: {queue_url}")
        print("Message ID:", response['MessageId'])

    except Exception as e:
        print(f"Error sending message to SQS queue {queue_url}: {e}")

if __name__ == "__main__":
    # Specify the SQS queue URL
    queue_url = input("Enter the SQS Queue URL: ")
    
    # Specify the message body
    message_body = input("Enter the message body: ")

    send_message_to_sqs(queue_url, message_body)
