from django.urls import path
from . import views
from .views import home, register_player, player_list, registered_players, get_all_players
from .views import custom_login


urlpatterns = [
     path('login/', custom_login, name='login'),
    # path('register/', views.register, name='register'),
    path('', views.home, name='home'),
    path('register/', views.register_player, name='register_player'),
    path('players/', views.player_list, name='player_list'),
    path('api/players/', get_all_players, name='get_all_players'),
    path('registered_players/', views.registered_players, name='registered_players'),
    path('players/<int:pk>/edit/', views.update_player, name='update_player'),
    path('players/<int:id>/delete/', views.delete_player, name='delete_player'),
    
]
