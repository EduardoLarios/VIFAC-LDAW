from django.contrib.auth.views import logout
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^', include('dashboard.urls', namespace='dashboard')),
    url(r'^expedientes/', include('records.urls', namespace = 'records')),
    url(r'^usuarios/', include('users.urls')),
    url(r'^donaciones/', include('donations.urls', namespace = "donations")),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/$',logout, {'next_page': '/usuarios/login'}),
    url(r'^escolar/', include('scholar.urls', namespace = 'scolar')),
    url(r'^rifas/', include('raffles.urls', namespace = 'raffles')),
    url(r'^escolar/', include('scholar.urls', namespace="scholar")),
    #url(r'^expediente_medico/', include('medical.urls', namespace="medical")),
]
