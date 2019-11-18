from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Forecast

from .serializers import ForecastSerializer


# Create your views here.
class WeatherIndexView(generics.ListAPIView):
    authentication_classes = (BasicAuthentication, )
    permission_classes = (IsAuthenticated, )
    serializer_class = ForecastSerializer
    queryset = Forecast.objects.get_queryset()

