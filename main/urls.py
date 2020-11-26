from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add),
    path('edit/<path:path>/form', views.edit),
    path('delete/<path:path>', views.delete),
    path('edit/<path:path>/<path:dependency>', views.view),
    path('<path:folder>', views.folder),
]
