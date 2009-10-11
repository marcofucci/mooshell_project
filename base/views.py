import os.path

from django.views import static
from django.conf import settings   
from django.http import Http404  

def serve_static( request, path, tool=None):
    for media in settings.MEDIA_DIRS:
        if os.path.exists(os.path.join(media,path)) and os.path.isfile(os.path.join(media,path)):
            return static.serve( request, path, media)
    raise Http404 