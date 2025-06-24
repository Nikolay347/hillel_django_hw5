from django.db import models
from django.contrib.auth import  get_user_model

from django.contrib.auth import get_user_model

# Create your models here.
class RequestStatistics(models.Model):
    user = models.OneToOneField(get_user_model(), related_name="request_statistics", on_delete=models.DO_NOTHING)
    requests = models.IntegerField(default=0)
    exceptions = models.IntegerField(default=0)

