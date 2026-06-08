from django.contrib import admin
from .models import my_user,todo

# Register your models here.

@admin.register(my_user)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['username','email','gender','age']


@admin.register(todo)
class todoAdmin(admin.ModelAdmin):
    list_display=['title','completed']