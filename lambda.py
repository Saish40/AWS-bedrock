import json
import boto3
from datetime import datetime

client = boto3.client("bedrock-runtime")
s3_client = boto3.client('s3')

S3_BUCKET_NAME = 'lambda40'

def lambda_handler(event, context):
    try:
        print("Received event:", event)
        
        if 'prompt' not in event:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing prompt in event'})
            }

        user_prompt = event['prompt']

        request_body = {
            "prompt": user_prompt,
            "temperature": 0.9,
            "max_tokens": 4000
        }

        response = client.invoke_model(
            body=json.dumps(request_body),
            contentType='application/json',
            accept='application/json',
            modelId='cohere.command-text-v14',
        )

        response_bytes = response['body'].read()
        response_string = json.loads(response_bytes)
        print("Model response:", response_string)
        s3_key = f"responses/{user_prompt}.txt"
        response_json = json.dumps(response_string, indent=2)

        s3_client.put_object(
            Bucket=S3_BUCKET_NAME,
            Key=s3_key,
            Body=response_json, 
            ContentType='text/plain'
        )
        return {
            'statusCode': 200,
            'body': json.dumps({
                'model_response': response_string,
                's3_location': f"s3://{S3_BUCKET_NAME}/{s3_key}"
            })
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
