from django.urls import path, include

from . import api_views

urlpatterns = [
    path('', api_views.WeatherIndexView.as_view(), name='weather_index'),
]