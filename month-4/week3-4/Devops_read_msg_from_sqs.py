# Read Messages from SQS Queue
# Problem: Write a script to read and delete messages from an SQS queue.
# Objective: Automate message processing.

# read_delete_sqs_messages.py
import boto3

def read_and_delete_messages_from_sqs(queue_url):
    # Create an SQS client
    sqs = boto3.client('sqs')

    try:
        while True:
            # Receive messages from the SQS queue
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,  # Max is 10
                WaitTimeSeconds=10  # Long polling
            )

            messages = response.get('Messages', [])
            
            if not messages:
                print("No more messages to process.")
                break

            for message in messages:
                print(f"Received message: {message['Body']}")

                # Delete the message after processing
                receipt_handle = message['ReceiptHandle']
                sqs.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=receipt_handle
                )

                print("Message deleted from queue.")

    except Exception as e:
        print(f"Error reading or deleting messages from SQS queue {queue_url}: {e}")

if __name__ == "__main__":
    # Specify the SQS queue URL
    queue_url = input("Enter the SQS Queue URL: ")

    read_and_delete_messages_from_sqs(queue_url)
