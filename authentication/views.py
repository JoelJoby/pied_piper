from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView

# Custom Login View
class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'
    redirect_authenticated_user = True

# Custom Signup View (Placeholder)
class SignupView(TemplateView):
    template_name = 'authentication/signup.html'

# Home View
class HomeView(TemplateView):
    template_name = 'authentication/index.html'

# Logout View (Using default but can be wrapped if needed for strict MVT)
class CustomLogoutView(LogoutView):
    next_page = 'login'
