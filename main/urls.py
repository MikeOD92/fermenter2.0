from django.urls import path
from .Views import recipe_views, user_views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('', recipe_views.getRoutes, name="routes"),

    path('recipes/', recipe_views.getRecipes, name="recipes"),
    path('recipes/<str:pk>', recipe_views.getRecipes, name="recipes"),
    path('recipes/create/', recipe_views.makeRecipe, name="new_recipe"),
    path('recipes/update/<str:pk>/', recipe_views.updateRecipe, name="upate_recipe"),
    path('recipes/delete/<str:pk>/', recipe_views.deleteRecipe, name="delete_recipe"),
    
    path('comments/create/', recipe_views.postComment, name="post_comment"),

    #### User Views ###################

    path('login', user_views.MyTokenObtainPairView.as_view(), name='token_obtain'),
    path('register', user_views.register, name="register"),
    path('users/', user_views.get_users, name="user_list"),
    path('users/friends', user_views.get_friends, name="friend_list" ),
    path('users/<str:pk>', user_views.get_users, name="view_user"),
]