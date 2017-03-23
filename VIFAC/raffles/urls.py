from django.conf.urls import url
from . import views

app_name = 'raffles'

urlpatterns = [

    # url(r'^registrar/$', views.index, name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^detalle_panfleta/(?P<pk>[0-9]+)/$', views.PanfletaEdit.as_view() , name='raffle_detail'),
    url(r'^nuevo_participante/$', views.nuevo_participante, name='nuevo_participante'),
    url(r'^(?P<participant_id>[0-9]+)/asignar_panfleta/$', views.assign_form, name='assign_panflet'),
]