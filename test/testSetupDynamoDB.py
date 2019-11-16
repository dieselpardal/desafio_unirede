import json
from src.setupDynamoDB import SetupDynamoDB


class TestSetupDynamoDB:

    def test_clientDB_not_empty(self):
        conn = SetupDynamoDB()
        dynamodb_client = conn.clientDB()
        response = dynamodb_client.list_tables()
        assert json.dumps(response) != ''

    def test_clientDB_most_that_zero(self):
        conn = SetupDynamoDB()
        dynamodb_client = conn.clientDB()
        response = dynamodb_client.list_tables()
        assert len(json.dumps(response)) > 0

    def test_DB_exist_table(self):
        conn = SetupDynamoDB()
        table_name_expected = 'TableNames_xxx'
        clientDB = conn.clientDB()
        if not conn.existTable(table_name_expected):
            table = conn.createTable(table_name_expected, clientDB)
            assert conn.existTable(table_name_expected)
            table.delete()

    def test_DB_not_exist_table(self):
        conn = SetupDynamoDB()
        table_name_expected = 'testtable_xxx'
        if conn.existTable(table_name_expected):
            conn.deleteTable(table_name_expected)

        assert not conn.existTable(table_name_expected)

