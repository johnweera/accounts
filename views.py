from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import SignupForm

def index(request):
    return render(request, 'accounts/index.html')


class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup_form.html'
    success_url = reverse_lazy('accounts:index')
