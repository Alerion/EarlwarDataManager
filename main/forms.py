from django import forms
from django_jsonforms.forms import JSONSchemaField


class NameForm(forms.Form):
    json = JSONSchemaField(
        schema='schema.json',
        options={"theme": "bootstrap4"}
    )