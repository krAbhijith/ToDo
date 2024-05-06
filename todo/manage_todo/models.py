from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low')
    ]

    title = models.CharField(max_length=50)
    desc = models.TextField()
    date_created = models.DateField(auto_now=False, auto_now_add=True)
    date_expire =  models.DateField()
    priority = models.IntegerField(choices=PRIORITY_CHOICES)
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title