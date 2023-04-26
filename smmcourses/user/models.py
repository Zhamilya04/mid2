from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    image = models.ImageField(upload_to='images/', null=True, max_length=255)
    owner = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)