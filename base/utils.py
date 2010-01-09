"""
Common used utilities
"""

import os.path
import time

from django.conf import settings   

def log_to_file(msg, request=None, filename='django_log'):
	" log to a file in directory specified in settings "
	if not hasattr(settings, "LOG_DIR"):
		return 
	if not settings.LOG_DIR:
		return
	if not os.path.isdir(settings.LOG_DIR):
		return

	path = os.path.join(settings.LOG_DIR, filename)
	
	file = open(path, 'a')
	if not isinstance(msg, str):
		msg = str(msg)

	timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
	if request:
		username = request.user.username if request.user.is_authenticated() else 'guest'
		username = ''.join(['<',username, '>\t'])

	else:
		username = ''
	msg = ''.join([username, msg])

	log = '  '.join([timestamp, msg, "\n"])
	file.write(log)
	file.close()
	
		

def separate_log(char='-*', count=30):
	log_to_file(char*count)
