import json
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.conf import settings

import requests

from weather.models import Forecast


class Command(BaseCommand):

    help = 'Fetch cape town weather forecast'

    def handle(self, *args, **kwargs):
        try:
            city = '{"cityId": "77107"}'

            weather_url = settings.WEATHER_API_URL
            r = requests.post(weather_url, data=city,
                              headers={'X-AjaxPro-Method': 'GetForecast15DayExpanded'})

            if r.status_code == 200:
                json_data = self.parse_data(r.text)
                self.save_forecasts(json_data['value']['Forecasts'])

                self.stdout.write(self.style.SUCCESS("Successfully completed retrieving cape town weather forecast"))
        except Exception as exception:
            self.stdout.write(self.style.ERROR("Unexpected error occurred {}".format(exception)))

    def parse_data(self, json_text):
        return json.loads(json_text)

    def get_day_forecast(self, date):
        return Forecast.objects.filter(date=date).first()

    def save_forecasts(self, forecasts):
        weather_forecasts = []
        for forecast in forecasts:
            date = datetime.now() + timedelta(days=int(forecast['DaySequence']))
            forecast_date = date.date()
            day_forecast = self.get_day_forecast(forecast_date)
            if not day_forecast:
                weather_forecasts.append(Forecast(**{
                    'date': forecast_date,
                    'wind': forecast['WindSpeed'],
                    'rain': forecast['Rainfall'],
                    'maximum_temperature': forecast['HighTemp'],
                    'minimum_temperature': forecast['LowTemp']
                }))
            else:
                day_forecast.wind = forecast['WindSpeed']
                day_forecast.rain = forecast['Rainfall']
                day_forecast.maximum_temperature = forecast['HighTemp']
                day_forecast.minimum_temperature = forecast['LowTemp']
                day_forecast.save()

        Forecast.objects.bulk_create(weather_forecasts)
