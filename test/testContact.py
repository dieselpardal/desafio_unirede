
from src.contact import Contact
import app
import unittest


class TestContact(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()

    def test_index_has_template(self):
        browser = self.app.get('/')
        assert browser.status == '200 OK'

    def test_index_has_title(self):
        browser = self.app.get('/')
        html = browser.get_data(as_text=True)
        assert '<title>PROJETO DE DESAFIO DIESEL</title>' in html

    def test_organization_has_json(self):
        organization_expected = {'organization': {
            'id': '08863df7431e45eea2b7a6c4e830a8ef',
            'name': 'Carine Diesel',
            'groups': []
        }
        }
        way = Contact()
        organization = way.CRUDOrganization()
        assert organization == organization_expected

    def test_group_has_json(self):
        group_expected = {'group': [{
            'id': '01163df6631e45eea2b7a6c4e830a8rr',
            'owner': 'user email',
            'name': 'Some name',
            'contacts_list': [
                {
                    'name': 'Contact alias',
                    'details': [
                        {
                            'data': 'phone number',
                            'type': 'whatsApp'
                        },
                        {
                            'data': 'smth@yahoo.com',
                            'type': 'email'
                        },
                        {
                            'data': 'other phone number',
                            'type': 'telegram'
                        }
                    ]
                }
            ]
        }
        ]
        }
        way = Contact()
        group = way.createGroup()
        assert group == group_expected

    def test_group_id_has_json(self):
        id_expected = '01163df6631e45eea2b7a6c4e830a8rr'
        way = Contact()
        id = way.getByIdGroup()
        assert id == id_expected

    def test_group_is_deleted(self):
        expected = {}
        way = Contact()
        group = way.deleteGroup()
        assert group == expected
