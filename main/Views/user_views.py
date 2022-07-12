from ast import Return
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
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
    print(request.data)
    try: 
        user = CustomUser.objects.create(
            username = data['username'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            password = make_password(data['password'])
        )
        serializer = CustomUserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
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
@permission_classes([IsAuthenticated])
def friend_list(request, pk=None):

    user = request.user.id

    friendlist = CustomUser.objects.get(id=user).friends.all()

    serializer = CustomUserSerializer(friendlist, many=True)

    return Response(serializer.data) 

@api_view(['GET'])
def profile_view(request, username = None):
    if username:
        user = CustomUser.objects.get(username = username)
        serializer = CustomUserSerializer(user)

        return Response(serializer.data) 
        
    user = CustomUser.objects.get(id = request.user.id)

    serializer = CustomUserSerializer(user)

    return Response(serializer.data) 

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def send_friendrequest(request, friendId):
    from_user = request.user
    to_user = CustomUser.objects.get(id=friendId)
    friend_request, created = Friend_Request.objects.get_or_create(from_user = from_user, to_user = to_user)
    if created:
        return Response('Friend request sent.')
    else:
        return Response('Friend Request already sent.')

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def accept_friendrequest(request, requestId):
    friend_request = Friend_Request.objects.get(id=requestId)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return Response('accepted')
    else:
        return Response('friend Request not accepted')
