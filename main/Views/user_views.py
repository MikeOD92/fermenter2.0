from ast import Return
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from ..serializers.user_serializers import *
from ..models import * 

from django.contrib.auth.hashers import make_password

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

@api_view(['POST'])
def register(request):
    data = request.data

    try: 
        user = CustomUser.objects.create(
            username = data['username'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = TokenObtainPairSerializer(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_password(request):
    user = request.user

    if request.data['password'] != request.data['password_confirm']:
        raise exceptions.ValidationError('Passwords do not match')

    user.password = make_password(request.data['password'])
    user.save()
    serializer = CustomUserSerializer(user)
    return Response(serializer.data)

@api_view(['GET'])
def get_users(request, pk=None):

    users = CustomUser.objects.all()
    friendlist = CustomUser.objects.get(id=request.user.id).friends.all()

    if pk:
        user = CustomUser.objects.get(id=pk)
        if user in friendlist:
            serializer = CustomUserSerializer(user, many=False)
            return Response(serializer.data)

        serializer = NonFriendUserSerializer(user, many=False)
        return Response(serializer.data)

    serializer = NonFriendUserSerializer(users, many=True)

    return Response(serializer.data) 

@api_view(['GET'])
def friend_list(request, pk=None):

    user = request.user.id

    friendlist = CustomUser.objects.get(id=user).friends.all()

    serializer = CustomUserSerializer(friendlist, many=True)

    return Response(serializer.data) 

@api_view(['GET'])
def profile_view(request):

    user = CustomUser.objects.get(id = request.user.id)

    serializer = CustomUserSerializer(user)

    return Response(serializer.data) 

