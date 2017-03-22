from django.conf.urls import url
from . import views

urlpatterns = [
    
    # url(r'^registrar/$', views.index, name='index'),

    url(r'^$', views.index, name='index'),
    url(r'^donadores/$', views.new_donor, name='new_donor'),
    url(r'^lista_donadores/$', views.list_donor, name='list_donors'),
    url(r'^lista_categorias/$', views.list_category, name='list_category'),
    url(r'^lista_donaciones/$', views.list_donation, name='list_donation'),
    url(r'^donaciones/$', views.new_donation, name='new_donation'),
    url(r'^categorias/$', views.new_category, name ='new_category')
]
