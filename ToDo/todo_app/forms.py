from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task

class RegisterForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']

class TaskForm(forms.ModelForm):

    class Meta:
        model=Task

        fields=[
            'task',
            'description',
            'due_date',
            'priority',
            'is_completed'
        ]

    widgets={
        'task':forms.TextInput(attrs={
            'placeholder':'Enter task name'
        }),
        'description':forms.Textarea(attrs={
            'placeholder':'Description'
        }),
        'due_date':forms.DateInput(attrs={
            'type':'date'
        }),
        'priority':forms.Select(),

        'is_completed':forms.CheckboxInput()

    }
