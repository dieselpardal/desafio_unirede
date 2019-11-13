PROJETO DE DESAFIO DIESEL
=
- versão 1.0 por desenovlvedor Full Stack **Ivan Diesel**
- dieselpardal@gmail.com
- whatsapp 51991453527

### VERSÃO
- Python: 3.7.2
- Brew: Homebrew 2.0.3
- virtualenv: 16.7.7
- pip: 19.3.1
- aws: aws-cli/1.16.279 Python/3.7.2 Darwin/18.5.0 botocore/1.13.15
- http: 1.0.3
- chalice: chalice 1.12.0, python 3.7.2, darwin 18.5.0
- Boto3: 
- PyTest: 5.2.2

### Project premises

1.	Use provisioned repository; **OK**
2.	Python 3; **OK**
3.	Chalice - Python Serverless Microframework for AWS 
(https://github.com/aws/chalice), 
(https://chalice.readthedocs.io/en/latest/), 
(https://chalice-workshop.readthedocs.io/en/latest/index.html); **OK**
4.	Boto 3 - AWS SDK for Python; **OK**
5.	Integrate with Dynamodb using Boto 3;
6.	Pytest - Python testing tool; **OK**
7.	Create README.md with project setup; **OK**
8.	PEP8 - Styleguide; **OK**
9.	Validate JSON fields;
10.	 Build DynamoDB Structure and document it;
11.	 Use Boto 3 to Integrate with AWS DynamoDB;
12.	 Create environment file; **OK**
13.	 Create gitignore file; **OK**

### Objective:
1.	Allow email group registration to use for some application.
2.	Build a restful backend microservice

### Tasks
1.	Create Organization model;
2.	Create Group model;
3.	Create ContactsList model;
4.	Create Contact model;
5.	Create Dynamodb table called "cloudservices_usersgroups”;
6.	Route for CRUD Organization;

```JSON
 {
  "organization": {
    "id": “08863df7431e45eea2b7a6c4e830a8ef”,
    "name": "Some name",
    "groups": []
  }
}
```

7. Route Create Group (POST Method)
```JSON
{
  "group": {
    "id": “01163df6631e45eea2b7a6c4e830a8rr”,
    "owner": "user email",
    "name": "Some name",
    "contacts_list": [
      {
        "name": "Contact alias",
        "details": [
          {
            "data": "phone number",
            "type": "whatsApp"
          },
          {
            "data": "smth@yahoo.com",
            "type": "email"
          },
          {
            "data": "other phone number",
            "type": "telegram"
          }
        ]
      }
    ]
  }
}
```


8.	Route Delete Group (DELETE Method)
9.	Route Get All Groups (GET Method)
10.	Route Get Group By Id (GET Method)
11.	Route Update Group (PUT Method)

Model fields:

Object        | Name         | Type         | Description of validations|
------------- | -------------| -------------| --------------------------|
organization  | id           | String       | A valid uuid4.            |
.             | name         | String       | A valid String.           |
.             | groups       | Array        | A valid Array of group.   |
group         | id           | String       | A valid uuid4.            |
.             | owner        | String       | A valid email.            |
.             | name         | String       | A valid String.           |
.             | contacts_list| Array        | A valid Array of contac. |
contact       | name         | String       | A valid String.           |
.             | details      | Array        | A valid Array of detail.  |
detail        | data         | String       | A valid phone number or email.|
.             | type         | Enum         |  A valid Enum (WHATSAPP, EMAIL, TELEGRAM).|


---
# ESCOPO:

### OBJETIVO
O desafio de trabalho de Projeto é que permite a controlar os dados e a funcionalidade de todos os componentes,
frameworks e variáveis ao acordo de desafio.

### RESUMO DE COMPONENTES NECESSÁRIOS

- CHALICE: permite criar e implantar rapidamente aplicativos que usam o Amazon API Gateway e o AWS Lambda.
- AWS: Amazon Web Services, também conhecido como AWS, é uma plataforma de serviços de computação em nuvem, que formam uma plataforma de computação na nuvem oferecida pela Amazon.com.
- BOTO3: tem waiters para APIs de cliente e de recurso. O boto3 é fornecido com vários recursos específicos de serviços, como transferências multipart automáticas para o Amazon S3 e condições de consulta simplificadas para o Amazon DynamoDB.
- DynamoDB‎: é um serviço de banco de dados NoSQL proprietário totalmente gerenciado que suporta estruturas de dados de documentos e valores-chave e é oferecido pela Amazon.com como parte do portfólio da Amazon Web Services.
- Pytest: estrutura de teste que nos permite escrever códigos de teste usando python. 
- PEP8: oferece convenções para o código Python compreendido pela biblioteca padrão de projeto que acompanha a distribuição.

### DESENVOLVIMENTO
Entendimento e execução do escopo, organização, execução de códigos,
uso de técnicas de programação, padrões de projeto e nível de documentação.

### INSTALAÇÃO

1) Plartaforma IDE: PyCharm Python Pure versão 2018.3, atualiza à 29 de Janeiro de 2019.
2) Chalice :
Create a virtual enviornment:  
```
$ pip install virtualenv
$ virtualenv ~/.virtualenvs/chalice-demo
$ source ~/.virtualenvs/chalice-demo/bin/activate
```
Install chalice
```
$ pip install chalice
```

3) AWS:
```
$ pip install awscli
$ aws configure --profile dieselpardal
$ aws iam list-groups

```
Colocar chave e senha. para novo chave,
link: https://docs.aws.amazon.com/pt_br/cli/latest/userguide/cli-chap-configure.html
Criação de Administrador e usuario dieselpardal no grupo de Administrador com permissão.

4) HTTP:
```
$ sudo pip install --upgrade httpie
$ http httpie.org
```

5) TREE>
```
$ brew install tree
```

6) Boto3:
```
$ pip install boto3
```
7) PyTest:
```
pip install pytest
py.test -h
```

8) PEP8:
```
pip install pep8
```

9) ENV:
```
npm install dotenv --save
```

### Criação de Usuário e Administrador no AWS

no site AWS, criou novo usuario *dieselpardal* e *administrator no credenciais ao acordo de documento de boto3. 
O problema é que não tenho uma cartão de credito por isso não poderíamos continuar os processos de comando `chalice deploy`. 


### Para Executar:
```
$ chalice deploy
```

### fonte:
- https://github.com/jakubroztocil/httpie/issues/500
- https://pypi.org/project/boto3-python3/
- https://www.guru99.com/pytest-tutorial.html
- https://wiki.python.org.br/GuiaDeEstilo
- https://pep8.org/
- https://aws.amazon.com/pt/dynamodb/


