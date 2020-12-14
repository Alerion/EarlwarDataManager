from django import forms
from django_jsonforms.forms import JSONSchemaField as BaseJSONSchemaField, JSONEditorWidget as BaseJSONEditorWidget
from django.conf import settings

JSONEDITOR_JS_URL = 'https://cdn.jsdelivr.net/npm/@json-editor/json-editor@latest/dist/jsoneditor.js'


class JSONEditorWidget(BaseJSONEditorWidget):
    class Media:
        extend = False
        js = (
            JSONEDITOR_JS_URL,
        )


class JSONSchemaField(BaseJSONSchemaField):

    def __init__(self, schema, options, ajax=True, *args, **kwargs):
        forms.CharField.__init__(self, *args, **kwargs)

        self.schemadir = getattr(settings, 'JSONFORMS_SCHEMA_DIR', settings.STATIC_ROOT)
        self.backvalidate = getattr(settings, 'JSONFORMS_SCHEMA_VALIDATE', True)

        self.schema = self.load(schema)

        if ajax:
            self.widget = JSONEditorWidget(schema=schema, options=options)
        else:
            self.options = self.load(options)
            self.widget = JSONEditorWidget(schema=self.schema, options=self.options)


class JsonForm(forms.Form):
    json = forms.Field

    def __init__(self, schema: str, *args, **kwargs):
        super(JsonForm, self).__init__(*args, **kwargs)
        self.fields["json"] = JSONSchemaField(
            schema=schema,
            options={
                "theme": "bootstrap4",
                "iconlib": "fontawesome4",
                "disable_edit_json": True,
                "array_controls_top": True,
                "remove_button_labels": True,
                "disable_array_delete_all_rows": True,  # FIXME
                "ajax": True
            }
        )
