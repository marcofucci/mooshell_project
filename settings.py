# Django settings for AquaGallery project.
import re
import os

# default settings 
# (may be overwritten by machine_settings)
GOOGLE_ANALYTICS_ID = None
GOOGLE_VERIFICATION_META_TAG = None
CACHE_BACKEND = 'dummy://'
CACHE_MIDDLEWARE_KEY_PREFIX = "MooTools"
CACHE_MIDDLEWARE_SECONDS = 1800

MEDIA_PATHS=['mooshell']
DEBUG = False 
TEMPLATE_DEBUG = DEBUG

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'
MEDIA_ROOT = ''
MEDIA_URL = ''

# Get the machine specific settings:
from machine_settings import *
from mooshell.settings import *
from mooshell.machine_settings import *

if DEBUG:
    CACHE_BACKEND = 'dummy://'

ADMINS = (
		# ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

INTERNAL_IPS = ('127.0.0.1',)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = WEBDIR #os.path.join(MEDIA_ROOT)

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/adminmedia/'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',	
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
#	'django.core.context_processors.i18n',
    "django.core.context_processors.request",
    "mooshell.context_processors.load_settings",
) 

AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',	
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admindocs',
	'django.contrib.admin',
	'mooshell',
)
