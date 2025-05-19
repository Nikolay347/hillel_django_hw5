from django.db import models
from django.utils.functional import cached_property


class Department(models.Model):
    name = models.CharField(max_length=200)
    parent_department = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    @cached_property
    def position_count(self):
        return self.position_set.filter(is_active=True).count()

    def __str__(self):
        return self.name