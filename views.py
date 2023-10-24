from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm
from django.contrib.auth import views as auth_views

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    success_url = reverse_lazy('home:index')
