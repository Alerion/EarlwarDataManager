from django.conf import settings
from EarlwarDataManager.tree.tree import Tree
from EarlwarDataManager.file.file import get_json
from EarlwarDataManager.path.path import get_edit_path
from EarlwarDataManager.path.path import get_root


class Table:

    SETTINGS_FIELDS = [
        {'field': 'Link', 'title': 'Link', 'formatter': 'linkFormatter'},
        {'field': 'Error', 'title': 'Error'},
    ]

    def __init__(self, path: str):
        self.files = Tree().get_items(path)
        self.result = []
        self.fields = settings.FIELDS[get_root(path)] + self.SETTINGS_FIELDS

    def prepare(self, file):
        try:
            data = get_json(file['href'])
            data['Path'] = get_edit_path(file['href'])
        except Exception as err:
            data = {'Error': file['href'] + ' ' + format(err)}
        self.result.append(data)

    def get(self):
        for file in self.files:
            self.prepare(file)

        return {'columns': self.fields, 'data': self.result, 'showColumns': True}
