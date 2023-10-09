from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login, logout
from django.contrib import messages
from music_player.models import *
from django.contrib.auth import update_session_auth_hash
# Create your views here.



# Авторизация
def sign_in(request):
    valid_user = True
    form = SignInForm() 
    if request.method == 'POST':
        form = SignInForm(data = request.POST)        
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_staff and not user.is_superuser:
                return redirect('staff:home')
            
            return redirect('music_player:home')
        
        valid_user = False
    # form = SignInForm()    
    return render(request, 'sign_in.html', {'form': form, 'valid_user': valid_user})
    



# Регистрация 
def sign_up(request):
    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('users:sign_in')
    return render(request, 'sign_up.html', {'form': form})


# Выйти с профиля
def sign_out(request):
    logout(request)
    return redirect('users:sign_in')


def reset_password(request):
    form = ResetPasswordForm(request.user, request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('users:sign_in')
    return render(request, 'reset_password.html', {'form': form})
