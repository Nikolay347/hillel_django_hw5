from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    birth_date =  models.DateField(null=True, blank=True)
    hire_date =  models.DateField(null=True, blank=True)
    position = models.ForeignKey("Position", on_delete=models.SET_NULL, null=True)