from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^WebDev/', include('WebDev.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^adminmedia/(?P<path>.*)$', 'base.views.serve_static', name='adminmedia'),
    (r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'base.views.serve_static', name='media'),
    (r'^', include('machine_urls')),
)
