from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django_jsonforms.forms import JSONSchemaForm
from django.shortcuts import render

from .forms import NameForm


def index(request):
    return render(request, 'base.html')
