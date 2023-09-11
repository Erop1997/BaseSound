from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from .models import *
from .forms import *


def home(request):
    albums = request.GET.get('albums')
    songs = Song.objects.all()

    songs = Song.objects.filter(album=albums) if albums else songs

    return render(request, 'home.html', {'songs':songs})

def song(request,pk):
    music = Song.objects.get(pk=pk)
    return render(request, 'song.html', {'song': music})


@login_required(login_url='/users/sign_in')
def upload(request):
    form = SongForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('music_player:home')
    return render(request, 'upload.html', {'form': form})
from django.shortcuts import render
import os
from .models import *


def home(request):
    albums = request.GET.get('albums')
    songs = Song.objects.all()

    songs = Song.objects.filter(album=albums) if albums else songs

    return render(request, 'home.html', {'songs':songs})

def song(request,pk):
    music = Song.objects.get(pk=pk)
    return render(request, 'song.html', {'song': music})