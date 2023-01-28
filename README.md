# todo-list-aws
![GitHub top language](https://img.shields.io/github/languages/top/my-study-area/todo-list-aws)
[![Feito por](https://img.shields.io/badge/made%20by-adriano%20avelino-gree)](https://github.com/adrianoavelino)
[![Tamanho do repositório](https://img.shields.io/github/repo-size/my-study-area/todo-list-aws)](https://img.shields.io/github/repo-size/my-study-area/todo-list-aws)
[![Último commit do Github](https://img.shields.io/github/last-commit/my-study-area/todo-list-aws)](https://github.com/my-study-area/desafio-terraform-curso-docker/commits/main)

API Gateway e lambda de um To do list

## Tecnologias
- python
- docker e docker-compose

## Iniciando o projeto
```bash
# clona o respoitório
git clone https://github.com/my-study-area/todo-list-aws.git

# entra no diretório
cd todo-list-aws

# para configurar os valores do profile default da AWS
# Obs: AWS_ACCESS_KEY_ID e AWS_SECRET_ACCESS_KEY devem ter o valor `local`
aws configure --profile default

# inicia o dynamodb
docker-compose up -d

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

# lista as tabelas utilizando o profile default
aws --endpoint-url http://0.0.0.0:8000 dynamodb list-tables

# lista as tabelas definindo as váriaveis de ambiente
env AWS_ACCESS_KEY_ID=local AWS_SECRET_ACCESS_KEY=local \
aws --region us-east-1 dynamodb \
--endpoint http://localhost:8000 \
list-tables

# cria o ambiente virtual
python -m venv venv

# ativa o ambiente virtual no fish shell
source venv/bin/activate.fish
```
Para visualizar o dynamodb admin acesse [http://localhost:8001](http://localhost:8001)

Para executar localmente execute:
```bash
python run.py
```

## Links
- [Código de exemplo da função python](https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-apigateway-code.html#services-apigateway-code-python)
- [Todo Application](https://aws.github.io/chalice/samples/todo-app/index.html)
- [Python Boto3 and Amazon DynamoDB Programming Tutorial](https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/)
- [DynamoDB Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
