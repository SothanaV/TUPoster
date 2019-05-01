"""
WSGI config for web project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

_DEV_STATE = 'dev'
state = os.environ.setdefault("STATE", 'production')
if state == _DEV_STATE:
    os.environ["DJANGO_SETTINGS_MODULE"] = "web.settings.dev"
elif state == 'production':
    os.environ["DJANGO_SETTINGS_MODULE"] = "web.settings.production"

application = get_wsgi_application()
