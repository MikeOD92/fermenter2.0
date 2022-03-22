from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import * 

@api_view(['GET'])
def get_users(request, pk=None):

    users = CustomUser.objects.all()
    if pk:
        user = CustomUser.objects.get(id=pk)
        serializer = CustomUserSerializer(user, many=False)
        return Response(serializer.data)

    serializer = CustomUserSerializer(users, many=True)

    return Response(serializer.data) 

# @api_view(['GET'])
# def get_friends(request):
