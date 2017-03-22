from django.conf.urls import url
from . import views

app_name = 'raffles'

urlpatterns = [

    # url(r'^registrar/$', views.index, name='index'),

    url(r'^$', views.index, name='index'),
    #url(r'^lista_rifas/$', views.new_donor, name='new_donor'),
    #url(r'^nuevo_participante/$', views.list_donor, name='list_donors'),
    #url(r'^(?P<pk>[0-9]+)/nueva_panfleta/$', views.new_donation, name='new_donation'),
]