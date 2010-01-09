import os.path

from django.views import static
from django.conf import settings   
from django.http import Http404  

def serve_static(request, path, media='media', type=None):
	if type: 
		path = '/'.join([type, path])
		
	for media_group in settings.MEDIA_PATHS:
		media_path = os.path.join(settings.FRAMEWORK_PATH, media_group, media)
		file = os.path.join(media_path,path)
		if os.path.exists(file) and os.path.isfile(file):
			return static.serve( request, path, media_path)
		
	raise Http404 
