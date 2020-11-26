from django import forms


class AddForm(forms.Form):
    name = forms.TextInput()
    path = forms.HiddenInput()
