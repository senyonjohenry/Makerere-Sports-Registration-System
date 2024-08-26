from django.shortcuts import render, redirect
from .forms import PlayerForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Player
from .serializers import PlayerSerializer
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Use Django's built-in UserCreationForm for registration
        if form.is_valid():
            user = form.save()
            # Automatically log in the user after registration
            login(request, user)
            return redirect('home')  # Redirect to home or any other page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to the home page or another page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def register_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()

    return render(request, 'players/register_player.html', {'form': form})

@login_required
def home(request):
    return render(request, 'players/home.html')

@login_required
def player_list(request):
    query = request.GET.get('q')
    if query:
        players = Player.objects.filter(
            Q(student_name__icontains=query) |
            Q(main_sport__icontains=query)
        )
    else:
        players = Player.objects.all()
    return render(request, 'players/player_list.html', {'players': players})

@login_required
def registered_players(request):
    return render(request, 'registered_players.html')

@api_view(['GET'])
def get_all_players(request):
    players = Player.objects.all()
    serializer = PlayerSerializer(players, many=True)
    return Response(serializer.data)

@login_required
def update_player(request, pk):
    player = get_object_or_404(Player, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'players/update_player.html', {'form': form})



@login_required
def delete_player(request, id):
    player = get_object_or_404(Player, id=id)
    
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')  # Redirect to the player list or another relevant page
    
    return render(request, 'confirm_delete.html', {'player': player})


