import json
import random
from lambda_function import TABLE_NAME, create, handler
import boto3

id = random.randint(1, 100)
dynamo = boto3.resource('dynamodb', endpoint_url="http://localhost:8000").Table(TABLE_NAME)

event_body = {
  'operation': 'create',
  "descricao": f'descricao {id}'
}
event_create = {
  "body": json.dumps(event_body)
}

task_criada = create(dynamo, payload=event_body)
id_task = json.loads(task_criada.get('body')).get('id')
event_body = {
  'operation': 'read',
  "id": id_task
}
event_read = {
  "body": json.dumps(event_body)
}

event_body = {
  'operation': 'read',
  "id": "id nao encontrado"
}
event_read_not_found = {
  "body": json.dumps(event_body)
}

event_body = {'operation': 'invalida'}
event_invalid_operation = {
  "body": json.dumps(event_body)
}

event = {
  'operation': 'update',
  "id": id_task,
  'descricao': f'update-{id}'
}
event_update = {
  "body": json.dumps(event)
}

event = {
  'operation': 'update',
  "id": "notfound",
  'descricao': f'update-{id}'
}
event_update_not_found = {
  "body": json.dumps(event)
}

event = {
  'operation': 'delete',
  "id": "96549f56-9798-11ed-8c0d-283a4d9332d9"
}
event_delete = {
  "body": json.dumps(event)
}
context = None

# response = handler(event_create, context)
# response = handler(event_read, context)
# response = handler(event_read_not_found, context)
# response = handler(event_invalid_operation, context)
# response = handler(event_update, context)
# response = handler(event_update_not_found, context)
response = handler(event_delete, context)
print(response)
