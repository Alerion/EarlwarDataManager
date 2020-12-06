from django.urls import path
import main.views.filesystem
import main.views.common

urlpatterns = [
    path('edit/<path:path>/form', main.views.common.edit),

    path('icon/<path:path>', main.views.filesystem.view_icon),
    path('add/file', main.views.filesystem.add),
    path('add/folder', main.views.filesystem.add_folder),
    path('rename/file', main.views.filesystem.rename),
    path('delete/<path:path>', main.views.filesystem.delete),
    path('edit/<path:path>/<path:dependency>', main.views.filesystem.view),

    path('', main.views.common.index, name='index'),
    path('<path:path>', main.views.common.table),
]
