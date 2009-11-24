import os.path
import re

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'xxx'

ADMIN_EMAIL = 'john@doe.name'
ADMIN_FIRSTNAME = 'John'
ADMINLASTNAME = 'Doe'

FRAMEWORK_PATH = os.path.dirname(os.path.dirname(__file__)) +'/'
DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = '../database.db'     # Or path to database file if using sqlite3.
DATABASE_USER = ''
DATABASE_PASSWORD = ''
DATABASE_HOST = ''
DATABASE_PORT = ''

TIME_ZONE = 'Europe/London'
LANGUAGE_CODE = 'en'
LANGUAGES = (
	('en', 'English'),
	('pl', 'Polish'),
)
DEFAULT_LANGUAGE = 1

WEBDIR = 'mooshell_project/media/'
MEDIA_ROOT = os.path.join(FRAMEWORK_PATH, WEBDIR)

EMAIL_HOST = 'localhost'
TEMPLATE_DIRS = (
				 os.path.join(FRAMEWORK_PATH, 'mooshell/templates'),
				 os.path.join(FRAMEWORK_PATH, 'mooshell-project/templates'),
)
MEDIA_DIRS = (
			  MEDIA_ROOT,
				os.path.join(FRAMEWORK_PATH, 'mooshell_project/adminmedia/')
)

# uncomment if memcached available 
# CACHE_BACKEND = 'memcached://127.0.0.1:11211/'