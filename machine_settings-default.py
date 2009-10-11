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

DATABASE_ENGINE = 'mysql'
# sqlite3
DATABASE_NAME = 'tools'     # Or path to database file if using sqlite3.
DATABASE_USER = 'x'
DATABASE_PASSWORD = 'x'
DATABASE_HOST = 'localhost'
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
)


SEO_TITLE_TAIL = " | to test your JavaScript code"
SEO_TITLE_HEAD = ""

TITLE_SEPARATOR = " | "

PROJECT_NAME = "MooShell"
PROJECT_STATUS = "(local)"


