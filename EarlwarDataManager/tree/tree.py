from django.conf import settings
import os
from EarlwarDataManager.path.path import get_path

EXCLUDED_DIRS = [
    'JSONSchemas'
]

ENABLED_EXTS = [
    '.json'
]


class Tree:

    def prepare_item(self, name: str, path: str):
        if name.endswith(tuple(ENABLED_EXTS)):
            return {
                'text': name,
                'href': path,
            }

        return False

    def prepare_folder(self, name: str, path: str):
        os.chdir(settings.PATH + path)
        if os.path.isdir(name) and name not in EXCLUDED_DIRS:
            return {
                    'text': name,
                    'icon': 'fa fa-folder',
                    'href': get_path(path, name),
                    'nodes': self.get(get_path(path, name)),
                }

        return False

    def get(self, path=''):
        lists = []
        folders = []
        os.chdir(settings.PATH + path)
        for item in os.listdir():
            prepared = self.prepare_folder(item, path)
            if prepared:
                folders.append(prepared)
                continue
            prepared = self.prepare_item(item, f'/edit{path}/{item}/form')
            if prepared:
                lists.append(prepared)

        return folders + lists

    def get_items(self, path=''):
        lists = []
        os.chdir(settings.PATH + path)
        for item in os.listdir():
            os.chdir(settings.PATH + path)
            prepared = self.prepare_item(item, get_path(path, item))
            if prepared:
                lists.append(prepared)
            if os.path.isdir(item) and item not in EXCLUDED_DIRS:
                lists = lists + self.get_items(get_path(path, item))

        return lists
