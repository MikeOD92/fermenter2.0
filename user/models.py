from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="upload/profile_pic")

class Friend(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='friend_list')
    friend = models.ManyToManyField(CustomUser, related_name="friend" )

