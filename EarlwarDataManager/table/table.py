import json
import codecs
from django.conf import settings
from EarlwarDataManager.tree.tree import Tree


class Table:

    def __init__(self, path: str):
        self.files = Tree().get_items(path)
        self.result = []
        self.fields = settings.FIELDS[path.split('\\')[1]]

    def prepare(self, file):
        with codecs.open(settings.PATH + file["href"], "r", "utf-8-sig") as f:
            read_data = f.read()
            self.result.append(json.loads(read_data))

    def get(self):
        for file in self.files:
            self.prepare(file)

        return {"columns": self.fields, "data": self.result, "showColumns": True}
