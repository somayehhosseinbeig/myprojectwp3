from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def somayeh(request):
    return HttpResponse("Hello Somayeh")

def arnika(request):
    return HttpResponse("Hello Arnika")

def greet(request, name):
    return HttpResponse(f"Hello, {name.capitalize()}!")