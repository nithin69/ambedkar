from django.conf.urls import patterns, url, include
from eyeworld import models, views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                       url(r'^contactus/$', views.contactus, name='contactus'),
                       url(r'^brands/$', views.brands, name='brands'),
                       url(r'^aboutus/$', views.aboutus, name='aboutus'),
                       url(r'^services/$', views.services, name='services'),
                       url(r'^sun/$', views.sun, name='sun'),
                       url(r'^gallery/$', views.gallery, name='gallery'),
                       url(r'^frames/$', views.frames, name='frames'),
                       url(r'^lens/$', views.lens, name='lens'),

)


