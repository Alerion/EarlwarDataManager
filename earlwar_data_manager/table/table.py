from django.conf import settings
from earlwar_data_manager.tree.tree import Tree
from earlwar_data_manager.file.file import get_json
from earlwar_data_manager.path.path import get_root


class Table:

    SETTINGS_FIELDS = [
        {'field': 'Link', 'title': 'Actions', 'formatter': 'linkFormatter'},
        {'field': 'Error', 'title': 'Error', 'visible': False},
    ]

    def __init__(self, path: str):
        self.files = Tree().get_items(path)
        self.result = []
        self.fields = settings.FIELDS[get_root(path)] + self.SETTINGS_FIELDS

    def prepare(self, file):
        try:
            data = get_json(file['href'])
            data['Path'] = file['href']
            data['Filename'] = file['text']
        except Exception as err:
            data = {'Error': file['href'] + ' ' + format(err)}
        self.result.append(data)

    def get(self):
        for file in self.files:
            self.prepare(file)

        return {'columns': self.fields, 'data': self.result, 'showColumns': True, 'buttons': 'buttons'}
