from rest_framework import serializers
from django.contrib.auth.models import User 
from ..models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from .recipe_serializers import RecipeRelatedField

class CustomUserSerializer(serializers.ModelSerializer):

    recipe_list = RecipeRelatedField(many=True)
    # friends = FriendRelatedField(many=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'profile_pic', 'friends', 'recipe_list']
        extra_kawrgs = {
            'password' : { 'write_only' : True}
        }

class NonFriendUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username', 'first_name', 'last_name', 'profile_pic', 'friends']

class CustomUserSerializerWithToken(CustomUserSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ['id', 'username','first_name', 'last_name', 'email', 'profile_pic', 'friends', 'password', 'token']
        extra_kawrgs = {
            'password' : { 'write_only' : True}
        }

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token)

######## CUSTOM TOKEN SERIALIZER 
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        serializer = CustomUserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v

        return data

