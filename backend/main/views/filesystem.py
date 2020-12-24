import os

from django.conf import settings
from django.http import JsonResponse, HttpResponseRedirect, FileResponse

from earlwar_data_manager.file.file import get_json, put_json
from earlwar_data_manager.form.add import AddForm
from earlwar_data_manager.path.path import get_relative_path


def view(request, path: str, dependency: str):
    return JsonResponse(get_json(os.path.join(settings.JSON_SCHEMAS_PATH, dependency)))


def view_icon(request, path: str):
    path = os.path.join(settings.RESOURCES_PATH, path + '.png')
    if os.path.isfile(path):
        return FileResponse(open(path, 'rb'))

    return HttpResponseRedirect('/static/images/no_image.png')


def rename(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            dir_name = os.path.dirname(form.cleaned_data["old_name"])
            old_path = os.path.join(settings.RESOURCES_DATA_PATH, form.cleaned_data["old_name"])
            new_path = os.path.join(os.path.dirname(old_path), form.cleaned_data["name"])
            os.rename(old_path, new_path)
            return HttpResponseRedirect(get_relative_path(
                os.path.join('edit', dir_name, form.cleaned_data["name"], 'form')
            ))


def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            path = os.path.join(form.cleaned_data["path"], form.cleaned_data["name"])
            put_json({}, path)
            return HttpResponseRedirect(get_relative_path(os.path.join('edit', path, 'form')))


def add_folder(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            path = os.path.join(form.data["path"], form.data["name"])
            os.mkdir(os.path.join(settings.RESOURCES_DATA_PATH, path))
            return HttpResponseRedirect(get_relative_path(path))


def delete(request, path: str):
    os.unlink(os.path.join(settings.RESOURCES_DATA_PATH, path))
    return HttpResponseRedirect(get_relative_path(os.path.dirname(path)))
