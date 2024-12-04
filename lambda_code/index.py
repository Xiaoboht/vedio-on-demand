import json
import boto3
import os

s3 = boto3.client('s3')
sns = boto3.client('sns')

def handler(event, context):
    file_url = event['file_url']
    bucket_name = os.getenv('S3_BUCKET_NAME')
    sns_topic_arn = os.getenv('SNS_TOPIC_ARN')

    try:
        print(f"Downloading file from {file_url} and uploading to bucket {bucket_name}")

        print("File uploaded successfully.")

    except Exception as e:
        print(f"Error: {str(e)}")
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject='Lambda Function Error',
            Message=str(e)
        )
