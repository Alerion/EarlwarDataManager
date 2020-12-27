from django.conf import settings
from earlwar_data_manager.path.path import get_root
import os

EXCLUDED_DIRS = [
    'JSONSchemas'
]

ENABLED_EXTS = (
    '.json'
)


class Tree:

    def prepare_item(self, name: str, path: str):
        if name.endswith(ENABLED_EXTS):
            return {
                'name': name,
                'href': path,
                'type': get_root(path)
            }

        return False

    def prepare_folder(self, name: str, path: str, depth: int):
        os.chdir(os.path.join(settings.RESOURCES_DATA_PATH, path))
        if os.path.isdir(name) and name not in EXCLUDED_DIRS:
            return {
                    'name': name,
                    'depth': depth,
                    'href': os.path.join(path, name),
                    'children': self.get(os.path.join(path, name), depth+1),
                }

        return False

    def get(self, path='', depth=0):
        lists = []
        folders = []
        os.chdir(os.path.join(settings.RESOURCES_DATA_PATH, path))
        for item in os.listdir():
            prepared = self.prepare_folder(item, path, depth)
            if prepared:
                folders.append(prepared)
                continue
            prepared = self.prepare_item(item, os.path.join(path, item))
            if prepared:
                lists.append(prepared)

        return folders + lists

    def get_items(self, path=''):
        lists = []
        os.chdir(os.path.join(settings.RESOURCES_DATA_PATH, path))
        for item in os.listdir():
            os.chdir(os.path.join(settings.RESOURCES_DATA_PATH, path))
            prepared = self.prepare_item(item, os.path.join(path, item))
            if prepared:
                lists.append(prepared)
            if os.path.isdir(item) and item not in EXCLUDED_DIRS:
                lists = lists + self.get_items(os.path.join(path, item))

        return lists
