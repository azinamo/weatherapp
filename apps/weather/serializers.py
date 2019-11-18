from rest_framework import serializers

from .models import Forecast


class ForecastSerializer(serializers.ModelSerializer):

    wind_speed = serializers.SerializerMethodField()
    high_temperature = serializers.SerializerMethodField()
    low_temperature = serializers.SerializerMethodField()

    class Meta:
        model = Forecast
        fields = '__all__'

    def get_wind_speed(self, instance):
        return instance.wind_speed

    def get_high_temperature(self, instance):
        return instance.max_temperature

    def get_low_temperature(self, instance):
        return instance.min_temperature