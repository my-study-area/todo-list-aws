import random
from lambda_function import handler

id = random.randint(1, 100)
event_create = {
  'operation': 'create',
  "descricao": f"Descricao{id}"
}

event_read = {
  'operation': 'read',
  "id": "96549f56-9798-11ed-8c0d-283a4d9332d9"
}

event_read_not_found = {
  'operation': 'read',
  "id": "id nao encontrado"
}

event_update = {
  'operation': 'update',
  "id": "96549f56-9798-11ed-8c0d-283a4d9332d9",
  'descricao': f'update-{id}'
}

event_update_not_found = {
  'operation': 'update',
  "id": "notfound",
  'descricao': f'update-{id}'
}

event_delete = {
  'operation': 'delete',
  "id": "96549f56-9798-11ed-8c0d-283a4d9332d9"
}

context = None

# response = handler(event_create, context)
# response = handler(event_read, context)
# response = handler(event_read_not_found, context)
# response = handler({'operation': 'invalida'}, context)
# response = handler(event_update, context)
# response = handler(event_update_not_found, context)
response = handler(event_delete, context)
print(response)
