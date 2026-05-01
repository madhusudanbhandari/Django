from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegisterForm

# Create your views here.
def home(request):
    return render(request,"home.html")

def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    else:
        form=RegisterForm()
        
    return render(request,"register.html",{'form':form})

def login_view(request):
    return  render(request,"login.html")

def logout_view(request):
    return render(request,"logout.html")

def delete_view(request,id):
    return  render(request, "delete.html")