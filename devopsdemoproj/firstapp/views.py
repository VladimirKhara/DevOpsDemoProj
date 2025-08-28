from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse('This is the home page')

def about(request):
    return HttpResponse('This is the about2 page')

def test(request):
    return HttpResponse('This is the test12 page')