from django.shortcuts import render
import json
from django.contrib import messages
from EarlwarDataManager.tree.tree import Tree
from EarlwarDataManager.table.table import Table
from EarlwarDataManager.file.file import get_json
from EarlwarDataManager.file.file import put_json
from EarlwarDataManager.form.form import JsonForm
from django.http import JsonResponse
from EarlwarDataManager.path.path import get_root
from EarlwarDataManager.form.validator import validate
from django.conf import settings


def index(request):
    return render(request, 'tree.html', {'title': 'Tree view', 'data': json.dumps(Tree().get())})


def folder(request, folder: str):
    return render(request, 'table.html', {'title': folder, 'data': json.dumps(Table(folder).get())})


def edit(request, path: str):
    schema_type = settings.TYPES[get_root(path)]
    schema = get_json(schema_type)

    error = ""
    if request.method == 'POST':
        data = json.loads(request.POST['json'])
        try:
            validate(data, schema, request.build_absolute_uri())
            put_json(data, path)
            messages.add_message(request, messages.SUCCESS, 'Successfully changed')
        except Exception as err:
            error = format(err)
    else:
        data = get_json(path)

    return render(request, 'form.html', {
        'form': JsonForm(schema, initial={'json': data}),
        'title': path,
        "error": error.split('\n', 1)}
    )


def view(request, path: str, dependency: str):
    data = get_json(f'JSONSchemas\\{dependency}')

    return JsonResponse(data)
