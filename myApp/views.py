from django.shortcuts import render
from django.http import HttpRespose


# Create your views here.
def index(request):
  return HttpResponse("HTTP response")