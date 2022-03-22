from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import *

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = "__all__"

class FriendRealtedField(serializers.StringRelatedField):
    def to_representation(self, value):
        return FriendSerializer(value).data
    
    def to_internal_value(self, data):
        return data

class CustomUserSerializer(serializers.ModelSerializer):

    friend_list = FriendRealtedField(many=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'profile_pic', 'friend_list']