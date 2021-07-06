from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

def index(request):
    return render(request, 'accounts/index.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    else:
        return HttpResponse("Sorry") 

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')         

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/profile/')
        else:
            return HttpResponse("Sorry")    
    else:
        context = {'form':form}
        return render(request, 'accounts/register.html', context)    

# def register(request):
#     form = CreateUserForm()

#     if request.method == "POST":
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('/accounts/profile/')
#         else:
#             return HttpResponse("Sorry")    
#     else:
#         context = {'form':form}
#         return render(request, 'accounts/register.html', context)           