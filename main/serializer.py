from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'