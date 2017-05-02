from django.conf.urls import url
from . import views

app_name = 'medical'

urlpatterns = [

    # Generic URLs
    url(r'^$', views.index, name='index'),
    url(r'^nuevo/$', views.new_file, name='file_create'),
    url(r'^(?P<file_id>[0-9]+)/$', views.file_detail, name = 'file_detail'),
    url(r'^editar_expediente/(?P<pk>[0-9]+)/$', views.FileEdit.as_view(), name = 'file_update'),
    url(r'^borrar_expediente/(?P<file_id>[0-9]+)/$', views.file_delete, name = 'file_delete'),
    url(r'^agregar_registro/(?P<file_id>[0-9]+)/$', views.new_registro, name='add_register'),
    url(r'^editar_registro/(?P<registro_id>[0-9]+)/$', views.edit_registro, name='edit_register'),
    url(r'^borrar_registro/(?P<registro_id>[0-9]+)/$', views.registro_delete, name='registro_delete'),
    url(r'^agregar_laboratorio/(?P<file_id>[0-9]+)/$', views.new_lab, name='add_lab'),
    url(r'^editar_laboratorio/(?P<lab_id>[0-9]+)/$', views.edit_lab, name='edit_lab'),
    url(r'^eliminar_laboratorio/(?P<lab_id>[0-9]+)/$', views.lab_delete, name='lab_delete'),
    url(r'^agregar_ultrasonido/(?P<file_id>[0-9]+)/$', views.new_ultrasonido, name='add_us'),
    url(r'^editar_ultrasonido/(?P<us_id>[0-9]+)/$', views.edit_us, name='edit_us'),
    url(r'^borrar_ultrasonido/(?P<us_id>[0-9]+)/$', views.us_delete, name='us_delete'),
    url(r'^agregar_problema/(?P<file_id>[0-9]+)/$', views.new_problema, name = 'add_problem'),
    url(r'^editar_problema/(?P<problema_id>[0-9]+)/$', views.edit_problem, name = 'edit_problem'),
    url(r'^borrar_problema/(?P<problema_id>[0-9]+)/$', views.problema_delete, name = 'problem_delete'),
]
