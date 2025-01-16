from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

def home(request):
  return render(request, 'user/home.html')

def login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      return HttpResponse("Invalid credentials")
  return render(request, 'user/login.html')

def register(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    if User.objects.filter(username=username).exists():
      messages.error(request, "Username already exists. Please choose another.")
      return render(request, 'user/register.html')


    user = User.objects.create_user(
      username=username,
      password=password
    )
    user.save()

    user = authenticate(request, username=username, password=password)
    if user is not None:
      # log the user in
      login(request, user)
      messages.success(request, "Registration successful and you are now logged in.")
      return redirect('home')

    else:
      messages.error(request, "Authentication failed. Please try logging in.")
      return redirect('login')
      return render(request, 'user/register.html')

def logout_view(request):
  logout(request)
  return redirect('home')

