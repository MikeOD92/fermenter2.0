from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.get_users, name="user_list"),
    # path('users/friends', views.get_friends, name="friend_list" ),
    path('users/<str:pk>', views.get_users, name="view_user"),
    
]