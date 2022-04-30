from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from ..serializers.recipe_serializers import CommentSerializer, RecipeSerializer
from ..models import *
# General - View Routes

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

######### RECIPE VIEWS ##########

@api_view(['GET'])
def getRecipes(request, pk=None):

    friends = CustomUser.objects.get(id=request.user.id).friends.all()
    recipes = Recipe.objects.filter(user__in = friends)

    if pk:
        recipe = Recipe.objects.get(id=pk)
        if recipe.user in friends:
            serializer = RecipeSerializer(recipe, many=False)
            return Response(serializer.data)
        else:
            return Response({"message":"you must be friends with this user to view their recipe"})

            

    serializer = RecipeSerializer(recipes, many=True)

    return Response(serializer.data) 

@api_view(['GET'])
def myRecipes(request):

    recipes = Recipe.objects.filter(user = request.user.id)
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


######### Comments VIEWS ##########
@api_view(['POST'])
def postComment(request):
    serializer = CommentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)