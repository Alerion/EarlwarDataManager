from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<path:path>/form', views.edit),
    path('edit/<path:path>/<path:dependency>', views.view),
    path('<path:folder>', views.folder),
]
