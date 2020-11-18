from django import forms
from django_jsonforms.forms import JSONSchemaField


class JsonForm(forms.Form):
    json = forms.Field

    def __init__(self, schema: str, *args, **kwargs):
        super(JsonForm, self).__init__(*args, **kwargs)
        self.fields["json"] = JSONSchemaField(
            schema=schema,
            options={"theme": "bootstrap4", "ajax": True}
        )
        print(self.fields)
