__author__ = 'rt'

from django.conf.urls import patterns, url, include
from fly import views

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                url(r'^$', views.index, name='index'),
                url(r'^about/$', views.about, name='about'),
                url(r'^contact/$', views.contact, name='contact'),
                url(r'^blog/$', views.blog, name='blog'),
                url(r'^products/$', views.products, name='products'),
                url(r'^detail/$', views.detail, name='detail'),
                url(r'^cart/$', views.cart, name='cart'),
                url(r'^checkout/$', views.checkout, name='checkout'),
                url(r'^login/$', views.login, name='login'),
                url(r'^register/$', views.register, name='register'),
                url(r'^compare/$', views.compare, name='compare'),
                url(r'^wishlist/$', views.wishlist, name='wishlist'),        
               
               
                       
                       		      
)
