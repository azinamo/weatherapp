from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.WeatherIndexView.as_view(), name='weather_index'),
]