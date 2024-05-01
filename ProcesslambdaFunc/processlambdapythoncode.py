import json
import boto3

def lambda_handler(event, context):
    # Initialize SQS client
    sqs = boto3.client('sqs')
    
    # Process each record in the event
    for record in event['Records']:
        # Extract message body
        message_body = json.loads(record['body'])
        
        # Process message body (change this according to your use case)
        print("Received message:", message_body)
        
        # Perform your processing logic here
        
        # Delete the message from the queue
        try:
            sqs.delete_message(
                QueueUrl=record['eventSourceARN'],
                ReceiptHandle=record['receiptHandle']
            )
            print("Message deleted from the queue.")
        except Exception as e:
            print("Error deleting message from the queue:", e)

    return {
        'statusCode': 200,
        'body': json.dumps('Message processing completed.')
    }
