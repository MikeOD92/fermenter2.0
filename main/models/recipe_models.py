from django.db import models
from django.contrib.auth.models import User

# from backend.user.models import CustomUser
from user.models import CustomUser

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
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

