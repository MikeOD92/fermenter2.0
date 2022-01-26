from django.shortcuts import render
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

