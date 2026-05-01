from django.db import models

# Create your models here.
 
class Task(models.Model):
    task=models.CharField(max_length=250)
    description=models.TextField()
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    due_date=models.DateField()
    priority=models.CharField(
        max_length=10,
        choices=[('Low','Low'),('Medium','Medium'),('High','High')],
        default='Low'
    )


    def __str__(self):
        return self.task