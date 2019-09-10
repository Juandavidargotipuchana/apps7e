from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index(resques):
    return HttpResponse("Welcom to the market :: ")

def hello (resques):
    return HttpResponse(":: Hello everyone  :: ")