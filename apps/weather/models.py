from django.db import models
from django.utils.translation import ugettext as __


# Create your models here.
class Forecast(models.Model):

    date = models.DateField(
        verbose_name=__('Date')
    )
    minimum_temperature = models.PositiveIntegerField(
        verbose_name=__('Min Temperature')
    )
    maximum_temperature = models.PositiveIntegerField(
        verbose_name=__('Max Temperature')
    )
    wind = models.CharField(
        max_length=50
    )
    rain = models.CharField(
        max_length=20,
        verbose_name=__('Rainfall')
    )

    def __str__(self):
        return "{}".format(self.date)

    def get_absolute_url(self):
        return

    def temperature(self, value):
        return "{}C".format(value)

    @property
    def max_temperature(self):
        return self.temperature(self.maximum_temperature)

    @property
    def min_temperature(self):
        return self.temperature(self.minimum_temperature)

    @property
    def wind_speed(self):
        return "{}km/hr".format(self.wind)

