from django.conf.urls import url
from . import views

urlpatterns = [
	#/adopciones
	url(r'^$', views.index, name='index'),
	
	#/adopciones/45/
	url(r'^(?P<family_id>[0-9]+)/$', views.detail, name='detail'),
	
	#/adopciones/ver/
	url(r'^ver_familias$', views.read, name='read'),
	
	#/adopciones/agregarFamilia/
	url(r'^agregarFamilia/$', views.add_Family, name='add_Family'),
]
