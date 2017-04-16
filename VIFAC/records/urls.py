from django.conf.urls import url
from . import views

urlpatterns = [
    
    # Generic URLs
    url(r'^$', views.index, name = 'index'),
    
    # URLS for Expedientes
    url(r'^lista_expedientes/$', views.list_record, name = 'list_records'),
    url(r'^nuevo_expediente/$', views.new_record, name = 'new_record'),
    url(r'^borrar_expediente/(?P<pk>\d+)/$', views.RecordDelete, name = 'record_delete'),
    url(r'^editar_expediente/(?P<pk>\d+)/$', views.RecordUpdate.as_view(), name = 'record_update')
]
