from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from .models import *
from staff.models import *
from django.db.models import Q

from .forms import *


def home(request):
    albums = request.GET.get('albums')
    songs = Song.objects.all()
    my_songs = request.GET.get('add_my')
    search = request.GET.get('search')
    songs = Song.objects.filter(album=albums) if albums else songs
    songs = songs.filter(add_my=request.user) if my_songs else songs

    if search:
        songs = Song.objects.filter(
            Q(name__icontains=search)
            )
        return render(request, 'home.html', {'songs':songs, 'albums':albums})
    
    return render(request, 'home.html', {'songs':songs})

def added(request,pk):
    song_data = Song.objects.get(pk=pk)

    song_data.add_my.add(request.user) if request.user not in song_data.add_my.all() \
        else song_data.add_my.remove(request.user)
    return redirect('music_player:home')

def song(request,pk):
    music = Song.objects.get(pk=pk)
    
    return render(request, 'song.html', {'song': music})


@login_required(login_url='/users/sign_in')
def upload(request, pk):


    form = SongForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        album = Album.objects.get(pk=pk)
        instance.album = album
        instance.save()
        return redirect('music_player:home')
    return render(request, 'upload.html', {'form': form})

def choosing_album(request):
    albums = Album.objects.filter(is_uploaded=True)
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and album_form.is_valid():
        album_form.save()
        created_album = Album.objects.last()
        return redirect(f'music_player:upload', pk=created_album.pk )
    
    return render(request, 'choosing_album.html', {'albums':albums, 'album_form': album_form})
