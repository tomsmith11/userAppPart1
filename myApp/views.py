from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

# define home page, rendering home.html

def home(request):
  return render(request, 'user/home.html')

# Define login page, rendering login.html, using a request method
# of POST and authenticating the user if the details match a user in
# the database. If the user is authenticated, the user is logged in
# And if there is no such user, an error message is thrown.

def login_page(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)
    
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, "Invalid credentials")
  return render(request, 'user/login.html')

# Create register view, using a request method of POST and potentially creating a new users
# Gathers information from the form and posts it to the databse, if the username already exists
# or if the form is not filled out correctly, an error message is thrown and the user is not created.
# After the account is created, the user is redirected to the login page

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
    return redirect('login')
  return render(request, 'user/register.html')

# Working logout button, using the logout function from django.contrib.auth

def logout_view(request):
  logout(request)
  return redirect('home')

