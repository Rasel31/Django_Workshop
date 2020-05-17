from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse


def register(request):
    print(request.POST)
    return render(request , 'accounts/register.html')


def login(request):
    print(request.POST)
    return render(request , 'accounts/login.html')


def logout(request):
    return HttpResponseRedirect(reverse('index'))


def dashboard(request):
    return render(request , 'accounts/dashboard.html')