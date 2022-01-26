from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('recipes/', views.getRecipes, name="recipes"),
    path('recipes/<str:pk>', views.getRecipes, name="recipes"),
    path('recipes/create/', views.makeRecipe, name="new_recipe"),
    path('recipes/update/<str:pk>/', views.updateRecipe, name="upate_recipe")

]