from first_app.models import Employee

from django.core.management import BaseCommand

class Command(BaseCommand):
    help = "Activates all employees 'is_active' = True"

    def handle(self, *args, **kwargs):
        updated = Employee.objects.update(is_active = True)
        self.stdout.write(self.style.SUCCESS(f"Successfully updated {updated} employees."))
