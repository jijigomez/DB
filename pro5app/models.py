from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_TYPES = [
        ('admin', 'Admin'),
        ('regular', 'Regular User'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, choices=USER_TYPES, default='regular')

    def __str__(self):
        return f"{self.user.username} - {self.type}"
