from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MenuItem(models.Model):
        CATEGORY_CHOICES=[
                ('starter','Starter'),
                ('main','Main Course'),
                ('desert','Dessert'),
                ('drink','Drinks'),
        ]

        name=models.CharField(max_length=100)
        description=models.TextField()
        price=models.DecimalField(max_digits=6,decimal_places=2)
        category=models.CharField(max_length=20,choices=CATEGORY_CHOICES)
        image=models.ImageField(upload_to='menu/', blank=True,null=True)
        is_available=models.BooleanField(default=True)


        def __str__(self):
                return self.name
        
class Booking(models.Model):
    user       = models.ForeignKey(User, on_delete=models.CASCADE)
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    phone      = models.CharField(max_length=15)
    date       = models.DateField()
    time       = models.TimeField()
    guests     = models.PositiveIntegerField()
    message    = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"

class ContactMessage(models.Model):
    name       = models.CharField(max_length=100)
    email      = models.EmailField()
    subject    = models.CharField(max_length=200)
    message    = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}