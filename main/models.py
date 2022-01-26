from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    catagory = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=True)
    ingredients = models.TextField(blank=False, null=True)
    method = models.TextField(blank=False, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(blank=False, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)

