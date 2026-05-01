from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def addTask(request):
    task=request.post['task']
    Task.objects.create(task=task)
    return HttpResponse('Form is submitted')

