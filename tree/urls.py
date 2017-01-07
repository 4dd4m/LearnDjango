from django.conf.urls import url
from . import views


urlpatterns  = [

url(r'^dir/', views.direction, name='direction'),
url(r'^', views.show_genres, name='genre'),
url(r'^index/$', views.index, name='index'),


]