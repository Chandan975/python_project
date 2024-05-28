from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    roles = (
        ('admin', 'admin'),
        ('user', 'user'),
    )
    role = models.CharField(max_length=10, choices=roles, default='user')

class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
