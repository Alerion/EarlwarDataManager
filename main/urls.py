from django.urls import path
import main.views.filesystem
import main.views.common

urlpatterns = [
    path('edit/<path:path>/form', main.views.common.edit),

    path('add/file', main.views.filesystem.add),
    path('rename/file', main.views.filesystem.rename),
    path('add/folder', main.views.filesystem.add_folder),
    path('delete/<path:path>', main.views.filesystem.delete),
    path('edit/<path:path>/<path:dependency>', main.views.filesystem.view),

    path('', main.views.common.index, name='index'),
    path('<path:path>', main.views.common.table),
]
