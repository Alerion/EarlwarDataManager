from django.shortcuts import render
import json
from EarlwarDataManager.tree.tree import Tree
from EarlwarDataManager.table.table import Table
from EarlwarDataManager.file.file import get_json
from .form import JsonForm
from django.http import JsonResponse
from django.conf import settings


def index(request):
    return render(request, 'tree.html', {'title': 'Tree view', 'data': json.dumps(Tree().get())})


def folder(request, folder: str):
    folder = "\\" + folder.rstrip("/").replace("/", "\\")
    return render(request, 'table.html', {"title": folder, "data": json.dumps(Table(folder).get())})


def edit(request, path: str):
    path = "\\" + path.rstrip("/").replace("/", "\\")
    schema_type = settings.TYPES[path.split('\\')[1]]
    schema = get_json(schema_type)
    data = get_json(path)

    return render(request, 'form.html', {"form": JsonForm(schema, initial={"json": data}), "title": path})


def view(request, path: str, dependency: str):
    data = get_json("\\JSONSchemas\\" + dependency.rstrip("/").replace("/", "\\"))

    return JsonResponse(data)
