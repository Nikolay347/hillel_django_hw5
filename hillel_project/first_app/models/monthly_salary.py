from django.db import models


class MonthlySalary(models.Model):
    date = models.DateField()
    salary = models.IntegerField()
    bonus = models.IntegerField(null=True, blank=True)
    employee = models.ForeignKey("Employee", on_delete=models.DO_NOTHING)
    is_paid = models.BooleanField(default=False)