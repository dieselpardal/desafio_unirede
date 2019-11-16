
import json
from flask import render_template


class Contact:
    __organization = {'organization': {
        'id': '08863df7431e45eea2b7a6c4e830a8ef',
        'name': 'Carine Diesel',
        'groups': []
    }
    }

    __groupConst = {'group':
        [
            {
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

    __group = {}

    def __int__(self):
        self.__group = {}

    def main(self):
        return render_template('index.html')

    def CRUDOrganization(self):
        return self.__organization

    def createGroup(self):
        self.__group = self.__groupConst
        return self.__group

    def deleteGroup(self):
        self.__group = {}
        return self.__group

    def getByIdGroup(self):
        groups = self.__groupConst
        for group in groups['group']:
            ids = group['id']

        return ids

    def getAllGroups(self):
        return self.__group

    def convertList(self,response):
        result = ' '
        for i in response['Items']:
            result = '{0}{1} {2}  {3}   {4}   {5}{6}'.format(result, str(i['Id']), str(i['sortkey']), str(i['owner']),
                                                             str(i['name']), str(i['contacts_list']), str('<br/>'))

        return result

