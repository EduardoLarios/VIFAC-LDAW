from django.conf.urls import url
from . import views

urlpatterns = [
    
    # Generic URLs
    url(r'^$', views.index, name = 'index'),
    
    # URLS for Expedientes
    url(r'^lista_expedientes/$', views.list_record, name = 'list_records'),
    url(r'^nuevo_expediente/$', views.new_record, name = 'new_record'),
    url(r'^borrar_expediente/(?P<pk>\d+)/$', views.RecordDelete, name = 'record_delete'),
    url(r'^editar_expediente/(?P<pk>\d+)/$', views.RecordUpdate.as_view(), name = 'record_update'),
    url(r'^detalle_expediente/(?P<pk>\d+)/$', views.RecordDetailView.as_view(), name='record_detail'),
    url(r'^exportar_csv/$', views.export_records_csv, name='export_records_csv'),
    
    #URLS for Archivos
    url(r'^subir_documento/(?P<exp_id>[0-9]+)$', views.model_form_upload, name='upload_document'),
    url(r'^listar_documentos/(?P<exp_id>[0-9]+)$', views.list_documents, name='list_documents'),
    url(r'^download/(?P<path>.*)$', views.download, name='download'),
    url(r'eliminar_archivo/(?P<doc_id>[0-9]+)$', views.delete_document, name='delete_file'),
    
]
