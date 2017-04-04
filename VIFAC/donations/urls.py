from .views import CategoryDelete, DonorDelete, DonationDelete
from django.conf.urls import url
from . import views

urlpatterns = [
    
    #Generic URLs
    url(r'^$', views.index, name = 'index'),
    
    #URLs for Donors
    url(r'^nuevo_donador/$', views.new_donor, name='new_donor'),
    url(r'^lista_donadores/$', views.list_donor, name='list_donors'),
    url(r'^borrar_donador/(?P<pk>\d+)$', views.DonorDelete, name='donor_delete'),
    url(r'^editar_donador/(?P<pk>\d+)/$', views.DonorUpdate.as_view(), name="donor_update"),
    
    #URLs for Donations
    url(r'^lista_donaciones/$', views.list_donation, name='list_donations'),
    url(r'^nueva_donacion/$', views.new_donation, name='new_donation'),
    url(r'^borrar_donacion/(?P<pk>\d+)$', views.DonationDelete, name='donation_delete'),
    url(r'^editar_donacion/(?P<pk>\d+)/$', views.DonationUpdate.as_view(), name="donation_update"),
    
    #URLS for Categories
    url(r'^lista_categorias/$', views.list_category, name = 'list_categories'),
    url(r'^nueva_categoria/$', views.new_category, name = 'new_category'),
    url(r'^borrar_categoria/(?P<pk>\d+)$', views.CategoryDelete, name = 'category_delete'),
    url(r'^editar_categoria/(?P<pk>\d+)/$', views.CategoryUpdate.as_view(), name = "category_update")
]
