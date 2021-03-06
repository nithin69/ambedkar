__author__ = 'rt'

from django.conf.urls import patterns, url, include
from ampackers import views

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^about/$', views.about, name='about'),
                url(r'^contact/$', views.contact, name='contact'),
                url(r'^services/$', views.services, name='services'),
                url(r'^gallery/$', views.gallery, name='gallery'),
                url(r'^zohoverify/verifyforzoho.html/$', views.zohoverify, name='zohoverify'),
##                url(r'^email/$', views.email, name='email'),
##                url(r'^thanks/$', views.thanks, name='thanks'),   
                       
                   url(r'^notify/$', views.notify, name='notify'),      		      
)
