from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
  return render(request, 'user/home.html')

def login(request):
  return render(request, 'user/login.html')

def register(request):
  return render(request, 'user/register.html')

