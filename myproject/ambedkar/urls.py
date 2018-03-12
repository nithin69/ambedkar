from django.conf.urls import include, url, patterns
from django.contrib import admin
from ams import views, models
from django.conf import settings
#from freshmaza import *
#from fly import *


urlpatterns = [
    # Examples:
    # url(r'^$', 'ambedkar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
#    url(r'^soft/', include('soft.urls')),
    url(r'^occ/', include('oneclick.urls')),
    url(r'^fly/', include('fly.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^booking/', include('booking.urls')),
    url(r'^abvgk/', include('abvgk.urls')),
    url(r'^jfr/', include('lab.urls')),
    url(r'^aandv/', include('freshmaza.urls')),
    url(r'^ndt/', include('ndt.urls')),
    url(r'^newsapp/', include('newsapp.urls')),
    url(r'^', include('ams.urls')),
    url(r'^ampackers/', include('ampackers.urls')),
#    url(r'^calendar/', include('happenings.urls', namespace='calendar'))
    url(r'^eyeworld/', include('eyeworld.urls')),
    url(r'^media/(?P<path>.*)/$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]

if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
