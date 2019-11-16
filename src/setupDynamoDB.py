import boto3


class SetupDynamoDB:

    def __init__(self):
        pass

    def clientDB(self):
        return boto3.client('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    def resourceDB(self):
        return boto3.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")

    def existTable(self, table_name):
        clientDB = self.clientDB()
        existing_tables = clientDB.list_tables()['TableNames']
        return table_name in existing_tables

    def createTable(self, table_name, clientDB):
        response = clientDB.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'hashid',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'query',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'hashid',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'query',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        return response

    def deleteTable(self, table_name):
        resourceDB = self.resourceDB()
        if self.existTable(table_name):
            table = resourceDB.Table(table_name)
            table.delete()

    def createTableGroup(self, resourceDB):
        table_name = 'group'
        return resourceDB.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'Id',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'sortkey',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'Id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'sortkey',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5

            }

        )
