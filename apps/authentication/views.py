from django.contrib import messages
from django.views.generic import FormView, TemplateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.utils.translation import ugettext as __
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

from .forms import RegistrationForm


# Create your views here.
class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'authentication/login.html'


class RegistrationView(FormView):
    form_class = RegistrationForm
    template_name = 'authentication/registration.html'

    def form_valid(self, form):
        try:
            form.save()
            messages.success(self.request, __('User account successfully created'))
            return HttpResponseRedirect(reverse_lazy('login'))
        except Exception as exception:
            print("Exception occurred --> {}".format(exception.__str__()))
            messages.success(self.request, __('User account could not be created, please try again'))
        return HttpResponseRedirect(reverse_lazy('registration'))


class LogoutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('homepage'))

