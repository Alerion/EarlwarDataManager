from django import forms


class AddForm(forms.Form):
    name = forms.CharField()
    path = forms.CharField(widget=forms.HiddenInput)
    old_name = forms.CharField(widget=forms.HiddenInput, required=False)
