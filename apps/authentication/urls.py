from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
]