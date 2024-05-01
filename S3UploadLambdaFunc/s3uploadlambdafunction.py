import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Get the file from the request
    file_content = event['body']
    
    # Upload the file to S3
    try:
        s3.put_object(Bucket='mains3bucketnamessk', Key='file_name.txt', Body=file_content)
        return {
            'statusCode': 200,
            'body': json.dumps('File uploaded successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }
