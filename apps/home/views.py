from django.views.generic import TemplateView


# Create your views here.
class LandingView(TemplateView):
    template_name = 'home/landing.html'
