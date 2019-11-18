from django.contrib import admin

from .models import Forecast


# Register your models here.
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('date', 'minimum_temperature', 'maximum_temperature', 'wind', 'rain')


admin.site.register(Forecast, ForecastAdmin)