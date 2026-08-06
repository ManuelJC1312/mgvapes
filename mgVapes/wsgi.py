"""
WSGI config for mgVapes project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
import logging
from pathlib import Path
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mgVapes.settings')

# Initialize Django first
django_application = get_wsgi_application()

# Then run migrations as a safe initialization step
try:
    from django.core.management import execute_from_command_line
    import django
    django.setup()
    
    # Check if migrations need to be run
    from django.db import DEFAULT_DB_ALIAS, connections
    from django.db.migrations.executor import MigrationExecutor
    
    executor = MigrationExecutor(connections[DEFAULT_DB_ALIAS])
    plan = executor.migration_plan(executor.loader.graph.leaf_nodes())
    
    if plan:
        print("Running pending migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
except Exception as e:
    print(f"Migration initialization error (this may be expected): {e}")
    logging.exception("Error during migration initialization")

application = django_application
