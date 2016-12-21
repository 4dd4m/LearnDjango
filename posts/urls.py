from django.contrib import admin
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.post_list, name='index'),

    #/create/2000
    url(r'^create/$', views.post_create, name='create'),

    #/post/2000
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),
    
    #/edit/1000
    url(r'^(?P<slug>[\w-]+)/edit/$', views.post_update, name='update'),

    #/delete/1000
    url(r'^(?P<slug>[\w-]+)/delete/$', views.post_delete, name='delete'),
]
