from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def add_task(request):
    return render(request,'add_task/html')