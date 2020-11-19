from jsonschema import Draft4Validator, RefResolver
import os


def validate(data: dict, schema: dict, url: str):
    resolver = RefResolver(
        base_uri=url,
        referrer=schema
    )
    Draft4Validator.check_schema(schema)
    validator = Draft4Validator(schema, resolver=resolver, format_checker=None)
    validator.validate(data)
