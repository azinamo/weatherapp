from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from .models import Forecast


# Create your views here.
class WeatherIndexView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    template_name = 'weather/index.html'
    paginate_by = 3
    model = Forecast
    queryset = Forecast.objects.all()
    context_object_name = 'forecasts'

