import logging

from django.contrib.auth import user_logged_in
from django.core.exceptions import ValidationError
from django.core.signals import got_request_exception
from django.db.models.signals import pre_save
from django.dispatch import receiver

from first_app.models import Position

MIN_SALARY = 2222

logger = logging.getLogger("default")

@receiver(pre_save, sender=Position)
def fix_min_salary_limit(sender, instance, **kwargs):
   if instance.monthly_rate < MIN_SALARY:
       instance.monthly_rate = MIN_SALARY
       logger.info(f"Monthly rate for Position: '{instance.title}' was automatically increased up to limit")
       raise ValidationError(f"Monthly rate cant be lower than {MIN_SALARY}")


@receiver(got_request_exception)
def handle_request_exception(sender, request, **kwargs):
    exception_instance = kwargs.get("exception", None)
    logger.exception(f"Error while process request {request.path}: ")