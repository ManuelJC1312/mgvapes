"""
WSGI config for mgVapes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mgVapes.settings')

# Run migrations on startup (failsafe)
try:
    call_command('migrate', '--noinput', verbosity=0)
except Exception as e:
    print(f"Migration attempt: {e}")

application = get_wsgi_application()
