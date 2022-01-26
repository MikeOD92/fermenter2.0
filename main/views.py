from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializer import RecipeSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/recipes/',
        '/api/recipes/create/',

        '/api/recipes/<id>/comments/',

        '/api/recipes/<id>/',

        '/api/recipes/delete/<id>/',
        '/api/recipes/update/<id>/',
    ]
    return Response(routes)

@api_view(['GET'])
def getRecipes(request, pk=None):

    recipes = Recipe.objects.all()

    if pk:
        recipe = Recipe.objects.get(id=pk)
        serializer = RecipeSerializer(recipe, many=False)
        return Response(serializer.data)

    serializer = RecipeSerializer(recipes, many=True)

    return Response(serializer.data) 

@api_view(['POST'])
def makeRecipe(request):
    serializer = RecipeSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    serializer = RecipeSerializer(instance=recipe, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()

    return Response({
        'data': serializer.data
        }, status=status.HTTP_202_ACCEPTED)

@api_view(["DELETE"])
def deleteRecipe(request, pk):
    recipe = Recipe.objects.get(id=pk)
    recipe.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
