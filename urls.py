from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

try:
	import grappelli
	admin_urls = [
		(r'^grappelli/', include('grappelli.urls')),
	]
except:
	admin_urls = [
	]
urls = admin_urls
urls.extend([
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	(r'^', include('machine_urls'))
])

urlpatterns = patterns('',*urls)
