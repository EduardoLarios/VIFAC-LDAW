from django.conf.urls import url
from . import views
from .views import EscuelasListView

app_name = 'scholar'

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^nueva_escuela/$', views.nueva_escuela , name='new_school'),
    url(r'^lista_escuelas/$', EscuelasListView.as_view(), name='list_escuela')
]