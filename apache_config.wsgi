import os, sys
apache_configuration= os.path.dirname(__file__)
project = os.path.dirname(apache_configuration)
workspace = os.path.dirname(project)
sys.path.append(workspace)
sys.path.append('/usr/lib/python2.6/site-packages/django/')
sys.path.append('/directory-containing-mooshell-and-mooshell_project')
sys.path.append('/directory-containing-mooshell-and-mooshell_project/mooshell_project')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mooshell_project.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler() 
