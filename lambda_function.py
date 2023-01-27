import json
import random
import boto3
import uuid

TABLE_NAME = 'TodoList'

def lambda_handler(event, context):
  operation = event.get('httpMethod')
  dynamo = boto3.resource('dynamodb', endpoint_url="http://localhost:8000").Table(TABLE_NAME)

  operations = {
    'POST': lambda event: create(dynamo=dynamo, event=event),
    'GET': lambda event: read(dynamo=dynamo, event=event),
    'PUT': lambda event: update(dynamo=dynamo, event=event),
    'DELETE': lambda event: delete(dynamo=dynamo, event=event)
  }

  if operation in operations:
    resposta = operations[operation](event=event)
    return resposta
  else:
    return {
      "statusCode": 400,
      "body": json.dumps({"mensagem": f"Erro ao realizar a operação {operation}"}, ensure_ascii=False)
    }

def create(dynamo, event):
  id = str(uuid.uuid1())
  body = event.get('body')
  payload = json.loads(body)
  descricao = payload.get('descricao')
  item = { "id": id, "descricao": descricao }
  dynamo.put_item(Item=item)
  return {
    "statusCode": 201,
    "body": json.dumps(item, ensure_ascii=False)
  }

def read(dynamo, event):
  payload = event.get('pathParameters')
  id = payload.get('task_id')
  item = { "id": id }
  resposta = dynamo.get_item(Key=item)
  if not resposta.get('Item'):
    return {
      "statusCode": 404,
      "body": json.dumps({'error': 'Tarefa não encontrada'}, ensure_ascii=False)
    }
  return {
    "statusCode": 200,
    "body": json.dumps(resposta.get('Item'), ensure_ascii=False)
  }

def update(dynamo, event):
  payload = event.get('pathParameters')
  id = payload.get('task_id')
  body = event.get('body')
  payload = json.loads(body)
  descricao = payload.get('descricao')
  item = { "id": id }

  if(read(dynamo, event).get('statusCode') == 200):
    resposta = dynamo.update_item(
      Key=item,
      UpdateExpression="set descricao=:descricao",
      ExpressionAttributeValues={':descricao': descricao},
      ReturnValues="UPDATED_NEW"
    )
    item['descricao'] = descricao
    return {
      "statusCode": 200,
      "body": json.dumps(item, ensure_ascii=False)
    }

  return {
    "statusCode": 404,
    "body": json.dumps({'error': 'Tarefa não encontrada'}, ensure_ascii=False)
  }

def delete(dynamo, event):
  payload = event.get('pathParameters')
  id = payload.get('task_id')
  item = { "id": id }
  dynamo.delete_item(Key=item)
  return {
    "statusCode": 200
  }
