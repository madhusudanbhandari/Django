from django.urls import path
from . import views

urlpatterns=[
    path('register/',views.register,name='register'),
    path('login/',views.login, name='login'),
    path('todos/',views.todo_register, name='save_todo'),
    path('todos/<pk>/',views.update_todo, name='todo update'),
]