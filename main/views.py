import os

from django.shortcuts import render
from django.contrib import messages
from EarlwarDataManager.tree.tree import Tree
from EarlwarDataManager.table.table import Table
from EarlwarDataManager.file.file import *
from EarlwarDataManager.path.path import *
from EarlwarDataManager.form.edit import JsonForm
from EarlwarDataManager.form.add import AddForm
from django.http import JsonResponse, HttpResponseRedirect
from EarlwarDataManager.form.validator import Validator
from django.conf import settings

SCHEMA_PATH = 'JSONSchemas'


def index(request):
    return render(request, 'tree.html', {'title': 'Tree view', 'data': json.dumps(Tree().get())})


def folder(request, folder: str):
    add = AddForm()
    add.path = folder
    return render(request, 'table.html', {
        'title': folder,
        'data': json.dumps(Table(folder).get()),
        'add': add
    })


def edit(request, path: str):
    schema_type = settings.TYPES[get_root(path)]
    schema = get_json(f'{SCHEMA_PATH}/{schema_type}')

    error = ""
    if request.method == 'POST':
        data = json.loads(request.POST['json'])
        try:
            validator = Validator(schema, request.build_absolute_uri())
            validator.validate(data)
            put_json(data, path)
            messages.add_message(request, messages.SUCCESS, 'Successfully changed')
        except Exception as err:
            error = format(err)
    else:
        data = get_json(path)

    return render(request, 'form.html', {
        'form': JsonForm(schema_type, initial={'json': data}),
        'title': path,
        'back': get_folder(path),
        "error": error.split('\n', 1)}
    )


def view(request, path: str, dependency: str):
    data = get_json(f'{SCHEMA_PATH}/{dependency}')

    return JsonResponse(data)


def add(request):
    if request.method == 'POST':
        add = AddForm(request.POST)
        if add.is_valid():
            path = f'{add.data["path"]}/{add.data["name"]}'
            put_json({}, path)
            return HttpResponseRedirect(f'/edit/{path}/form')


def delete(request, path: str):
    os.unlink(settings.PATH + path)
    return HttpResponseRedirect(get_folder(path))
