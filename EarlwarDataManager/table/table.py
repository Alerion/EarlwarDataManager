from django.conf import settings
from EarlwarDataManager.tree.tree import Tree
from EarlwarDataManager.file.file import get_json


class Table:

    SETTINGS_FIELDS = [{"field": "Link", "title": "Link", "formatter": "linkFormatter"}]

    def __init__(self, path: str):
        self.files = Tree().get_items(path)
        self.result = []
        self.fields = settings.FIELDS[path.split('\\')[1]] + self.SETTINGS_FIELDS

    def prepare(self, file):
        data = get_json(file["path"])
        data["Path"] = "/edit" + file["path"] + "/form"
        self.result.append(data)

    def get(self):
        for file in self.files:
            self.prepare(file)

        return {"columns": self.fields, "data": self.result, "showColumns": True}
