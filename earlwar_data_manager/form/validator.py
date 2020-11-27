from django.conf import settings
from jsonschema import Draft4Validator, RefResolver
import os

from earlwar_data_manager.file.file import get_json


class Validator:
    def __init__(self, schema_type: str, url: str):
        self.schema = get_json(os.path.join(settings.JSON_SCHEMAS_PATH, schema_type))
        self.resolver = RefResolver(
            base_uri=url,
            referrer=self.schema
        )
        self.base_uri = url

    def validate(self, data: dict):
        Draft4Validator.check_schema(self.schema)
        validator = Draft4Validator(self.schema, resolver=self.resolver, format_checker=None)
        validator.validate(data)

    def resolve(self, schema_url: str):
        return self.resolver.resolve_from_url(schema_url)