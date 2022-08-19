import json
import boto3
import os

client = boto3.client('dynamodb')

table_name = os.getenv("TABLE_NAME")

def handler(event, _):
  body = json.loads(event['body'])
  
  data = client.put_item(
    TableName=table_name,
    Item={
        'id': {
          'S': body['id']
        },
        'name': {
          'S': body['name']
        }
    }
  )

  response = {
      'statusCode': 200,
      'body': json.dumps({"id": body['id'], "name":body['name']}),
      'headers': {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
  }
  
  return response