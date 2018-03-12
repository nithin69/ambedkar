from django.conf.urls import patterns, url, include
from newsapp import views
from views import *
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                url(r'^$', views.newsapp, name='newsapp'),
                url(r'^(?P<id>\d+)/$', views.single, name='single'),
)
