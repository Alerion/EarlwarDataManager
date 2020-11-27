from django.conf import settings
from earlwar_data_manager.tree.tree import Tree
from earlwar_data_manager.file.file import get_json
from earlwar_data_manager.path.path import get_root


class Table:

    SETTINGS_FIELDS = [
        {'field': 'Error', 'title': 'Error'},
        {'field': 'Link', 'title': 'Link', 'formatter': 'linkFormatter'},
    ]

    def __init__(self, path: str):
        self.files = Tree().get_items(path)
        self.result = []
        self.fields = settings.FIELDS[get_root(path)] + self.SETTINGS_FIELDS

    def prepare(self, file):
        try:
            data = get_json(file['href'])
            data['Path'] = file['href']
        except Exception as err:
            data = {'Error': file['href'] + ' ' + format(err)}
        self.result.append(data)

    def get(self):
        for file in self.files:
            self.prepare(file)

        return {'columns': self.fields, 'data': self.result, 'showColumns': True, 'buttons': 'buttons'}
