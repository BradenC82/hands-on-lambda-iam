import json
import boto3
import os

client = boto3.client('dynamodb')
table_name = os.getenv('TABLE_NAME')
def handler(event, _):

  data = client.get_item(
    TableName=table_name,
    Key={
        'id': {
          'S': event['pathParameters']['id']
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps(data),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response