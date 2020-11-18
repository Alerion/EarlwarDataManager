import json
from django.conf import settings
import codecs


def get_json(path: str):
    with codecs.open(settings.PATH + path, "r", encoding="utf-8-sig") as f:
        return json.loads(f.read().encode('utf-8'))