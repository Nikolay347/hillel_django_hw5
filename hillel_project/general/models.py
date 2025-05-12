from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.
class RequestStatistics(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="request_statistics", on_delete=models.DO_NOTHING)
    requests = models.IntegerField(default=0)
    exception = models.IntegerField(default=0)