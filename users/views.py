from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from music_player.models import *
from django.contrib.auth import update_session_auth_hash

# Авторизация
def sign_in(request):
    form = SignInForm(data = request.POST or None)        
    if form.is_valid:
        user = form.get_user()
        login(request, user)
        

        return redirect('music_player:home')
    return render(request, 'sign_in.html', {'form': form})


# Регистрация 
def sign_up(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid:
        form.save()
        return redirect('users:sign_in')
    return render(request, 'sign_up.html', {'form': form})
