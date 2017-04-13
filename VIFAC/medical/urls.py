from django.conf.urls import url
from . import views

urlpatterns = [

    # Generic URLs
    url(r'^$', views.index, name='index'),

]
