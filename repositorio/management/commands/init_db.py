from django.core.management.base import BaseCommand
from django.core.management import call_command
import os
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Initialize the database by running migrations'

    def handle(self, *args, **options):
        try:
            self.stdout.write("Starting database initialization...")
            call_command('migrate', '--noinput', verbosity=2)
            self.stdout.write(self.style.SUCCESS('Database initialization completed successfully'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Database initialization failed: {e}'))
            logger.error(f"Database initialization error: {e}")
