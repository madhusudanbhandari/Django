from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class my_user(AbstractUser):
    gender=models.TextField(max_length=10)
    age=models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
class todo(models.Model):
    user=models.ForeignKey(my_user,on_delete=models.CASCADE)
    title=models.TextField(max_length=40)
    description=models.TextField(max_length=200)
    completed=models.BooleanField(default=False)
    date=models.DateField()

    def __str__(self):
        return self.title
    