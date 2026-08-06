#!/usr/bin/env python
import os
import sys
import django
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mgVapes.settings')
    
    # Setup Django
    django.setup()
    
    # Run migrations
    print("=" * 60)
    print("Running database migrations...")
    print("=" * 60)
    try:
        execute_from_command_line(['manage.py', 'migrate', '--noinput', '--verbosity', '2'])
        print("✓ Migrations completed successfully")
    except Exception as e:
        print(f"✗ Migration error: {e}")
        sys.exit(1)
