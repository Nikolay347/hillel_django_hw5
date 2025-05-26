from django.contrib.auth.models import AbstractUser
from django.db import models

class Employee(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/",  null=True, blank=True)
    cv_file = models.FileField(upload_to="cvs/",  null=True, blank=True)
    birth_date =  models.DateField(null=True, blank=True)
    hire_date =  models.DateField(null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.SET_NULL, null=True)