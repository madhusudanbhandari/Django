from django.urls import path
from .views import studentList


urlpatterns=[
    path('students/',studentList.as_view()),
]