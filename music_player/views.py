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
    # all_songs = list(Song.objects.all())
    # songs_dict = {}
    # songs_dict['title'] = f'{music.name}'
    # songs_dict['file'] = f'/media/{music.song}'
    # songs_dict['poster'] = f'/media/{music.album.album_image}'
    # print(songs_dict)

    songs_dict = {'title': 'Monolit', 'file': '/media/Loc-Dog_ATL_-_Monolit_76049608_Dn8Fvfu_lcBjeAn_9qZqfDH_8jJvAFK_SyCntFV.mp3', 'poster': '/media/ATL_995I2n5.jpeg'}
    return render(request, 'song.html', {'song': music,'songs_dict':songs_dict})