from jsonschema import Draft4Validator, RefResolver
import os


class Validator:
    def __init__(self, schema: dict, url: str):
        self.resolver = RefResolver(
            base_uri=url,
            referrer=schema
        )
        self.base_uri = url
        self.schema = schema

    def validate(self, data: dict):
        Draft4Validator.check_schema(self.schema)
        validator = Draft4Validator(self.schema, resolver=self.resolver, format_checker=None)
        validator.validate(data)

    def resolve(self, schema_url: str):
        return self.resolver.resolve_from_url(schema_url)