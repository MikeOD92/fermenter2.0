from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

######## USER MODELS

class CustomUser(AbstractUser):
    username = models.CharField(max_length=500, unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to="upload/profile_pic", blank=True )
    friends = models.ManyToManyField("CustomUser", blank=True)

class Friend_Request(models.Model):
    from_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='to_user')

# Recipe Models
class Recipe(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name='recipe_list')
    catagory = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    ingredients = models.TextField(blank=False, null=True)
    method = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, null=True, related_name="comments")
    comment = models.TextField(blank=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

class RecipeImg(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name="recipe_images")
    img = models.ImageField(upload_to='upload/')

