import json
import boto3

client = boto3.client("bedrock-runtime")

def lambda_handler(event, context):

    print(event)
    user_prompt = event['prompt']

    response = client.invoke_model(
        body = json.dumps(
            {
                "prompt" : user_prompt,
                "temperature" : 0.9,
                "max_tokens" : 4000,
            }
        ),
        contentType = 'application/json',
        accept = 'application/json',
        modelId = 'cohere.command-text-v14',
    )
    print(response['body'])
    response_bytes = response['body'].read()
    response_string = json.loads(response_bytes)

    return {
        'statusCode': 200,
        'body': response_string
    }
