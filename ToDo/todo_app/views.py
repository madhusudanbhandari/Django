from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"home.html")

def register_view(request):
    return render(request,"register.html")

def login_view(request):
    return  render(request,"login.html")

def logout_view(request):
    return render(request,"logout.html")

def delete_view(request,id):
    return  render(request, "delete.html")