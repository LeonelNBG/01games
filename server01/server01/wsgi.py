import os
import sys

path = '/home/leonelNBG/01games/server01'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'server01.settings'

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
