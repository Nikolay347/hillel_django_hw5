from django.contrib import admin

from general.models import RequestStatistics


# Register your models here.
@admin.register(RequestStatistics)
class RequestStatisticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'requests')