import json
import random
import boto3
import uuid

TABLE_NAME = 'TodoList'

def handler(event, context):
  operation = event['operation']
  dynamo = boto3.resource('dynamodb', endpoint_url="http://localhost:8000").Table(TABLE_NAME)

  operations = {
    'create': lambda payload: create(dynamo=dynamo, payload=payload),
    'read': lambda payload: read(dynamo=dynamo, payload=payload),
    'update': lambda payload: update(dynamo=dynamo, payload=payload),
    'delete': lambda payload: delete(dynamo=dynamo, payload=payload)

  }

  if operation in operations:
    resposta = operations[operation](payload=event)
    return resposta
  else:
    return {
      "statusCode": 400,
      "body": json.dumps({"mensagem": f"Erro ao realizar a operação {operation}"}, ensure_ascii=False)
    }

def create(dynamo, payload):
  id = str(uuid.uuid1())
  descricao = payload.get('descricao')
  item = { "id": id, "descricao": descricao }
  dynamo.put_item(Item=item)
  return {
    "statusCode": 201,
    "body": json.dumps(item)
  }

def read(dynamo, payload):
  id = payload.get('id')
  item = { "id": id }
  resposta = dynamo.get_item(Key=item)
  if not resposta.get('Item'):
    return {
      "statusCode": 404,
      "body": json.dumps({'error': 'Tarefa não encontrada'})
    }
  return {
    "statusCode": 200,
    "body": json.dumps(resposta.get('Item'), ensure_ascii=False)
  }

def update(dynamo, payload):
  id = payload.get('id')
  descricao = payload.get('descricao')
  item = { "id": id }

  if(read(dynamo, payload).get('statusCode') == 200):
    resposta = dynamo.update_item(
      Key=item,
      UpdateExpression="set descricao=:descricao",
      ExpressionAttributeValues={':descricao': descricao},
      ReturnValues="UPDATED_NEW"
    )
    return {
      "statusCode": 200,
      "body": json.dumps(resposta)
    }

  return {
    "statusCode": 404,
    "body": json.dumps({'error': 'Tarefa não encontrada'}, ensure_ascii=False)
  }

def delete(dynamo, payload):
  id = payload.get('id')
  item = { "id": id }
  resposta = dynamo.delete_item(Key=item)
  return {
    "statusCode": 200
  }
