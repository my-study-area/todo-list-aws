import http
import json
import random
from lambda_function import TABLE_NAME, create, lambda_handler
import boto3

id = random.randint(1, 100)
dynamo = boto3.resource('dynamodb', endpoint_url="http://localhost:8000").Table(TABLE_NAME)
descricao = f"Descricao {id}"

event_body = {
  "descricao": descricao
}
event_create = {
  "httpMethod": "POST",
  "body": json.dumps(event_body)
}

task_criada = create(dynamo, event=event_create)
id_task = json.loads(task_criada.get('body')).get('id')
event_read = {
    "httpMethod": "GET",
    "pathParameters": {
      "task_id": id_task
    }
}


event_read_not_found = {
    "httpMethod": "GET",
    "pathParameters": {
        "task_id": 'id nao encontrado'
    }
}

event_invalid_operation = {
    "httpMethod": "PATCH"
}

event = {
  "id": id_task,
  "descricao": f"update-{id}"
}
event_update = {
    "httpMethod": "PUT",
    "pathParameters": {
      "task_id": id_task
    },
    "body": json.dumps(event)
}

event_update_not_found = {
    "httpMethod": "UPDATE",
    "pathParameters": {
      "task_id": 'id nao encontrada'
    },
  "body": json.dumps(event)
}


event_delete = {
  "httpMethod": "DELETE",
  "pathParameters": {
    "task_id": id_task
  }
}
context = None

response = lambda_handler(event_create, context)
# response = lambda_handler(event_read, context)
# response = lambda_handler(event_read_not_found, context)
# response = lambda_handler(event_invalid_operation, context)
# response = lambda_handler(event_update, context)
# response = lambda_handler(event_update_not_found, context)
# response = lambda_handler(event_delete, context)
print(response)
