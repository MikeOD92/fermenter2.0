from rest_framework import serializers
from django.contrib.auth.models import User 
from ..models import *
# from .user_serializers import UserRelatedField

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentRealtedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return CommentSerializer(value).data
    
    def to_internal_value(self, data):
        return data

class RecipeImageSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecipeImg
        fields='__all__'

class RecipeImageRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return RecipeImageSerializer(value).data

    def to_internal_value(self, data):
        return data

class RecipeSerializer(serializers.ModelSerializer):

    comments = CommentRealtedField(many=True)
    recipe_images = RecipeImageRelatedField(many=True)

    class Meta:
        model = Recipe
        fields = ['id','title', 'user', 'author', 'catagory', 'description', 'ingredients', 'method', 'comments', 'recipe_images']

# class MyRecipesSerializer(serializers.ModelSerializer):

class RecipeRelatedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return RecipeSerializer(value).data

    def to_internal_value(self, data):
        return data