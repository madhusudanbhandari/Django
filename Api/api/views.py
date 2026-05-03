from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentsView(request):
    students={
        'id':2, 'name':'sita', 'age':43
    }
    return JsonResponse(students)