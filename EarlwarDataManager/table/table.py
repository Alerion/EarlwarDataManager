import json
import codecs
from django.conf import settings
from EarlwarDataManager.tree.tree import Tree

class Table:

    FIELDS = [
        "Id",
        "Name"
    ]

    def __init__(self, path: str):
        self.files = Tree().get_items(path)
        self.result = []

    def prepare(self, file):
        with codecs.open(settings.PATH + file["href"], "r", "utf-8-sig") as f:
            read_data = f.read()
            print(read_data)
            data = json.loads(read_data)

        prepared_data = {}
        for field in self.FIELDS:
            if field in data:
                prepared_data[field] = data[field]
        self.result.append(prepared_data)
        print(prepared_data)

    def get(self):
        for file in self.files:
            self.prepare(file)

        return self.result
