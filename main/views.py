from django.shortcuts import render
import json
from EarlwarDataManager.tree.tree import Tree
from EarlwarDataManager.table.table import Table


def index(request):
    return render(request, 'tree.html', {'title': 'Tree view', 'data': json.dumps(Tree().get())})


def folder(request, folder: str):
    folder = "\\" + folder.replace("/", "\\")
    return render(request, 'table.html', {"title": folder, "data": json.dumps(Table(folder).get())})
