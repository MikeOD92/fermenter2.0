from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('recipes/', views.getRecipes, name="recipes"),
    path('recipes/<str:pk>', views.getRecipes, name="recipes"),

]