from django.conf.urls import url
from . import views

app_name = 'medical'

urlpatterns = [

    # Generic URLs
    url(r'^$', views.index, name='index'),
    url(r'^nueva/$', views.new_file, name='file_create'),
    url(r'^(?P<file_id>[0-9]+)/$', views.file_detail, name = 'file_detail'),
    url(r'^editar/(?P<file_id>[0-9]+)/$', views.new_file, name = 'file_update'),
    url(r'^borrar/(?P<file_id>[0-9]+)/$', views.new_file, name = 'file_delete'),
    url(r'^agregar_registro/(?P<file_id>[0-9]+)/$', views.index, name='add_register'),
    url(r'^agregar_laboratorio/(?P<file_id>[0-9]+)/$', views.index, name='add_lab'),
    url(r'^agregar_ultrasonido/(?P<file_id>[0-9]+)/$', views.index, name='add_us'),
    url(r'^agregar_problema/(?P<file_id>[0-9]+)/$', views.index, name = 'add_problem'),
]
