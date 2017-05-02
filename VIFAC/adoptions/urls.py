from django.conf.urls import url
from . import views

urlpatterns = [
	#/adopciones
	url(r'^$', views.index, name='index'),

	#/adopciones/ver/
	url(r'^ver_familias$', views.read, name='read'),
	
	#/adopciones/agregarFamilia/
	url(r'^agregarFamilia/$', views.add_Family, name='add_Family'),
	
	#/adopcionesDelete
	url(r'^ver_familias/(?P<pk>[0-9]+)/delete/$', views.FamilyDelete, name='FamilyDelete')

]
