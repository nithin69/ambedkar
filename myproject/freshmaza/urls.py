__author__ = 'rt'

from django.conf.urls import patterns, url, include
from freshmaza import views,models

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^audio/$', views.audio, name='audio'),
                url(r'^contact/$', views.contact, name='contact'),
                url(r'^video/$', views.video, name='video'),
                url(r'^blog/$', views.blog, name='blog'),
##                url(r'^inner/$', views.inner, name='inner'),
                url(r'^inner/(?P<id>\d+)/$', views.inner, name='inner'),
                  

                       
                       
                       		      
)
