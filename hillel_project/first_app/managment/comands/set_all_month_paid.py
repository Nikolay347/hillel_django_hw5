from django.utils import timezone

from django.core.management import BaseCommand

from first_app.models import MonthlySalary


class Command(BaseCommand):
    help = "Set all salaries in this month 'is_paid' = True"

    def handle(self, *args, **options):
        current_month = timezone.now().month
        current_year = timezone.now().year

        salaries = MonthlySalary.objects.filter(
            date__month=current_month,
            date__year=current_year,
            is_paid=False
        )

        count = salaries.count()
        salaries.update(is_paid=True)
        self.stdout.write(
            self.style.SUCCESS(f"Command was successfully completed for {count} objects!")
        )