# todo-list-aws
To do list criado utilizando os recursos da AWS

```bash
# para configurar os valores do profile default da AWS
# Obs: AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY devem ter o valor `local`
aws configure --profile default

# inicia o dynamodb
docker-compose up -d

# lista as tabelas utilizando o profile default
aws --endpoint-url http://0.0.0.0:8000 dynamodb list-tables

# lista as tabelas definindo as váriaveis de ambiente
env AWS_ACCESS_KEY_ID=local AWS_SECRET_ACCESS_KEY=local \
aws --region us-east-1 dynamodb \
--endpoint http://localhost:8000 \
list-tables

# cria tabela TodoList
aws --endpoint-url http://localhost:8000 dynamodb create-table \
    --table-name TodoList\
    --attribute-definitions \
        AttributeName=id,AttributeType=S \
    --key-schema \
        AttributeName=id,KeyType=HASH \
    --provisioned-throughput \
        ReadCapacityUnits=10,WriteCapacityUnits=5 \
    --table-class STANDARD

# cria o ambiente virtual
python -m venv venv

# ativa o ambiente virtual no fish shell
source venv/bin/activate.fish
```

[Acesse o dynamodb admin](http://localhost:8001/)

Links:
- [https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-code.html#services-apigateway-code-python](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-code.html#services-apigateway-code-python)
- [Todo Application](https://aws.github.io/chalice/samples/todo-app/index.html)
- [Python Boto3 and Amazon DynamoDB Programming Tutorial](https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/)
- [](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
