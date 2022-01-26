from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import *

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentRealtedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return CommentSerializer(value).data
    
    def to_internal_value(self, data):
        return data

class RecipeSerializer(serializers.ModelSerializer):

    comments = CommentRealtedField(many=True)

    class Meta:
        model = Recipe
        fields = ['id','title', 'user', 'catagory', 'description', 'ingredients', 'method', 'comments']