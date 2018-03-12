from django.conf.urls import patterns, url, include
from oneclick import views
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^about/$', views.about, name='about'),
                url(r'^gallery/$', views.gallery, name='gallery'),
                url(r'^contact/$', views.contact, name='contact'),
                url(r'^occontact/$', views.occontact, name='occontact'),

)
