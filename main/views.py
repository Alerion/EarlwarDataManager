from django.shortcuts import render
from django.contrib import messages
from earlwar_data_manager.tree.tree import Tree
from earlwar_data_manager.table.table import Table
from earlwar_data_manager.file.file import *
from earlwar_data_manager.path.path import *
from earlwar_data_manager.form.edit import *
from earlwar_data_manager.form.add import *
from django.http import JsonResponse, HttpResponseRedirect
from earlwar_data_manager.form.validator import Validator
from django.conf import settings


def index(request):
    return render(request, 'tree.html', {'title': 'Tree view', 'data': json.dumps(Tree().get())})


def table(request, path: str):
    return render(request, 'table.html', {
        'title': path,
        'data': json.dumps(Table(path).get()),
        'add_form': AddForm(initial={'path': path})
    })


def edit(request, path: str):
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

    return render(request, 'form.html', {
        'form': JsonForm(schema_type, initial={'json': data}),
        'title': path,
        'back': get_folder(path),
        "error": error.split('\n', 1)}
    )


def view(request, path: str, dependency: str):
    return JsonResponse(get_json(os.path.join(settings.JSON_SCHEMAS_PATH, dependency)))


def add(request):
    if request.method == 'POST':
        add_form, = AddForm(request.POST)
        if add_form.is_valid():
            path = os.path.join(add_form.data["path"], add_form.data["name"])
            put_json({}, path)
            return HttpResponseRedirect(f'/edit/{path}/form')


def delete(request, path: str):
    os.unlink(os.path.join(settings.RESOURCES_DATA_PATH, path))
    return HttpResponseRedirect(get_folder(path))
