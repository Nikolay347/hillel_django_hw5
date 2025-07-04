from django.db import models
from django.utils.translation import gettext_lazy as _

class Position(models.Model):
    title = models.CharField(verbose_name=_("Title"), max_length=200)
    is_manager = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    description = models.CharField(verbose_name=_("Job Description"), max_length=500, default="")
    monthly_rate = models.IntegerField(default=0, verbose_name=_("Monthly Rate"))


    def __str__(self):
        return f"{self.title} ({self.department})"
