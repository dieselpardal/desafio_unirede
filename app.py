# PROJETO DE DESAFIO
# Versao 1.0
# Autor: desenvolvedor fullstack Ivan Diesel
# DIESEL 2019
# ----------------------------------------
# Esses codigos são somente de atividade de empresa. Não permitiu usar esses codigo para o uso.
# Autorização a licença somente para o autor.
#

import boto3
import decimal
import json

from flask import Flask, request
from uuid import uuid4
from src.contact import Contact
from src.setupDynamoDB import SetupDynamoDB
from src.serverConfig import ServerConfig

app = Flask(__name__)
app.debug = True
app.secret_key = str(uuid4())


@app.route('/')
@app.route('/index')
def index():
    way = Contact()
    return way.main()


@app.route('/organization')
def routeOrganization():
    way = Contact()
    return way.CRUDOrganization()


@app.route('/group', methods=["POST", "GET", "DELETE"])
def routeGroup():
    way = Contact()
    if request.method == "GET":
        return way.createGroup()

    if request.method == "DELETE":
        return way.deleteGroup()

    if request.method == "POST":
        return way.getAllGroups()

    return {}


@app.route('/group/<name>', methods=["GET", "PUT"])
def routePutGroup(name):
    way = Contact()
    if request.method == "PUT":
        return way.putGroup()

    if request.method == "GET" and name == 'id':
        return way.getByIdGroup()

    return {}


@app.route('/test')
def test():
    ddb = boto3.client('dynamodb', endpoint_url='http://localhost:8000/')
    return ddb.list_tables()


@app.route('/tablelist')
def tableList():
    conn = SetupDynamoDB()
    clientDB = conn.clientDB()
    response = clientDB.list_tables()
    return response


@app.route('/tablelistr')
def tableListr():
    conn = SetupDynamoDB()
    resourceDB = conn.resourceDB()
    response = resourceDB.list_tables()
    return response


@app.route('/create_table/cloudservices_usersgroups')
def createTableCloudServicesUsersGroups():
    conn = SetupDynamoDB()
    table_name = 'cloudservices_usersgroups'
    resourceDB = conn.resourceDB()
    if not conn.existTable(table_name):
        table = conn.createTable(table_name, resourceDB)
        return table.table_status
    else:
        return 'Tabela <b><i>cloudservices_usersgroups</i></b> já exsite.'


@app.route('/createtable/<table_name>', methods=["PUT"])
def createTable(table_name):
    conn = SetupDynamoDB()
    resourceDB = conn.resourceDB()
    if not conn.existTable(table_name):
        response = conn.createTable(table_name, resourceDB)
        return response
    else:
        return 'A tabela de <i>' + table_name + '</i> existiu.'


@app.route('/creategroup', methods=["POST"])
def createGroupTable():
    conn = SetupDynamoDB()
    resourceDB = conn.resourceDB()
    table_name = 'group'
    if not conn.existTable(table_name):
        conn.createTableGroup(resourceDB)
        return 'A tabela de <i>Group</i> e atribuites foram criadas.'
    else:
        return 'A tabela de <i>' + table_name + '</i> não existiu.'


@app.route('/scangroup', methods=["GET"])
def scanGroup():
    conn = SetupDynamoDB()
    way = Contact()
    resourceDB = conn.resourceDB()
    table_name = 'group'
    if conn.existTable(table_name):
        table_group = resourceDB.Table(table_name)
        response = table_group.scan()
        return way.convertList(response)
    else:
        return 'A tabela de <i>' + table_name + '</i> não existiu.'


@app.route('/loadgroup', methods=["PUT"])
def loadGroup():
    conn = SetupDynamoDB()
    way = Contact()
    resourceDB = conn.resourceDB()
    table_name = 'group'
    if conn.existTable(table_name):
        table_group = resourceDB.Table(table_name)
        with open("group.json", 'r') as json_file:
            groups = json.load(json_file, parse_float=decimal.Decimal)
            for group in groups['group']:
                id = str(uuid4())
                sortkey = str(uuid4())
                owner = group['owner']
                name = group['name']
                contacts_list = group['contacts_list']
                print("ID:" + id)
                response = table_group.put_item(
                    Item={
                        'Id': id,
                        'sortkey': sortkey,
                        'owner': owner,
                        'name': name,
                        'contacts_list': contacts_list,
                    }
                )

        return json.dumps(response, indent=4, cls=None)
    else:
        return 'A tabela de <i>' + table_name + '</i> não existiu.'


@app.route('/resetgroup', methods=["POST"])
def resetGroup():
    conn = SetupDynamoDB()
    resourceDB = conn.resourceDB()
    table_name = 'group'
    if conn.existTable(table_name):
        conn.deleteTable(table_name)

    conn.createTableGroup(resourceDB)
    return 'A tabela de <i>' + table_name + '</i> Reset.'


@app.route('/putgroup/<item_name>/<item_email>', methods=["PUT"])
def putGroup(item_name=None, item_email=None):
    conn = SetupDynamoDB()
    resourceDB = conn.resourceDB()
    table_name = 'group'
    if conn.existTable(table_name):
        table_group = resourceDB.Table(table_name)
        id = str(uuid4())
        sortkey = str(uuid4())
        response = table_group.put_item(
            Item={
                'Id': id,
                'sortkey': sortkey,
                'owner': item_email,
                'name': item_name,
                'contacts_list': [],
            }
        )
        return response
    else:
        return 'A tabela de <i>' + table_name + '</i> não existiu.'


@app.route('/deletetable/<table_name>', methods=["DELETE"])
def deleteTable(table_name):
    conn = SetupDynamoDB()
    if conn.existTable(table_name):
        conn.deleteTable(table_name)
    else:
        return table_name + ' NÃO EXISTE TABELA. <br/>Ok.'
    return 'A tabela de <i>' + table_name + '</i> foi deletado com sucesso.<br/>Ok.'


@app.route('/resource/<value>', methods=["PUT"])
def viewPut(value):
    return {"value": value}


if __name__ == "__main__":
    server = ServerConfig()
    serverPort = server.startServer()
    print("INICIO...")
    app.run(debug=True, port=serverPort, host='localhost')
