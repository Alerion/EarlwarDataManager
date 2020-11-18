from django.conf import settings
import os

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
                "text": name,
                "path": path + "\\" + name
            }

        return False

    def prepare_folder(self, name: str, path: str):
        os.chdir(settings.PATH + path)
        if os.path.isdir(name) and name not in EXCLUDED_DIRS:
            return {
                    "text": name,
                    "icon": "fa fa-folder",
                    "path": path + "\\" + name,
                    "nodes": self.get(path + "\\" + name),
                }

        return False

    def get(self, path=''):
        lists = []
        folders = []
        os.chdir(settings.PATH + path)
        for item in os.listdir():
            if self.prepare_folder(item, path):
                folders.append(self.prepare_folder(item, path))
                continue

            if self.prepare_item(item, path):
                lists.append(self.prepare_item(item, path))

        return folders + lists

    def get_items(self, path=''):
        lists = []
        os.chdir(settings.PATH + path)
        for item in os.listdir():
            os.chdir(settings.PATH + path)
            if self.prepare_item(item, path):
                lists.append(self.prepare_item(item, path))
            if os.path.isdir(item) and item not in EXCLUDED_DIRS:
                lists = lists + self.get_items(path + "\\" + item)

        return lists
