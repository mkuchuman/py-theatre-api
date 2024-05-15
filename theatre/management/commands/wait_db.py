from django.core.management.base import BaseCommand
from django.db import connections, OperationalError
from django.utils import timezone
import time


class WaitForDatabaseCommand(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Waiting for the database to start")
        db_conn = None
        start_time = timezone.now()
        while not db_conn:
            try:
                connection = connections['default']
                with connection.cursor() as cursor:
                    cursor.execute("SELECT 1")
                db_conn = connection
            except OperationalError:
                if timezone.now() - start_time > timezone.timedelta(minutes=1):
                    self.stdout.write(self.style.ERROR(
                        "Database took too long to start. Exiting."
                    ))
                    return
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))


class Command(WaitForDatabaseCommand):
    pass
