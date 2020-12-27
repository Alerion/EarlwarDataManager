import json
import os

from django.conf import settings
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render

from earlwar_data_manager.file.file import put_json, get_json
from earlwar_data_manager.form.edit import JsonForm
from earlwar_data_manager.form.validator import Validator
from earlwar_data_manager.path.path import get_root, get_relative_path
from earlwar_data_manager.table.table import Table
from earlwar_data_manager.tree.tree import Tree


def index(request):
    return JsonResponse({'items': Tree().get()})


def table(request):
    return JsonResponse(Table(request.GET.get('path')).get())


def edit(request):
    path = request.GET.get('path')
    schema_type = settings.TYPES[get_root(path)]

    error = ""
    if request.method == 'POST':
        data = json.loads(request.POST['json'])
        try:
            validator = Validator(schema_type, request.build_absolute_uri())
            validator.validate(data)
            put_json(data, path)
            messages.add_message(request, messages.SUCCESS, 'Successfully changed')
        except Exception as err:
            error = format(err)
    else:
        data = get_json(path)
    return JsonResponse(data)


def test(request):
    return render(request, 'test.html')