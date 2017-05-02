from django.conf.urls import url
from . import views

app_name = 'raffles'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^editar_panfleta/(?P<pk>[0-9]+)/$', views.PanfletaEdit.as_view() , name='raffle_detail'),
    url(r'^nuevo_participante/$', views.nuevo_participante, name='nuevo_participante'),
    url(r'^(?P<participant_id>[0-9]+)/panfletas/$', views.panfletas_part, name='panfletas_part'),
    url(r'^(?P<participant_id>[0-9]+)/asignar_panfleta/$', views.assign_form, name='assign_panflet'),
    url(r'^borrar_panfletas/$', views.delete_panfleta, name='panfleta_delete'),
    url(r'^borrar_participante/(?P<participant_id>[0-9]+)/$', views.delete_participante, name='borrar_participante'),
    url(r'^editar_participante/(?P<participant_id>[0-9]+)/$', views.delete_participante, name='borrar_participante'),

]
