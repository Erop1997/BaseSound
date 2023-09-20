from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from staff.models import *
from django.db.models import Q

from .forms import *


def home(request):

    return render(request, 'home.html', {})


def added(request,pk):
    song_data = Song.objects.get(pk=pk)

    song_data.add_my.add(request.user) if request.user not in song_data.add_my.all() \
        else song_data.add_my.remove(request.user)
    return redirect('http://127.0.0.1:8000/music_player/home/?homepage=tracks')
# Что тут добавить в редирект?
def songs(request):
    songs_list = Song.objects.all()
    my_songs = request.GET.get('add_my')
    songs_list = Song.objects.filter(add_my=request.user) if my_songs else songs_list
    return render(request, 'songs.html', {'songs_list':songs_list})

def song(request,pk):
    music = Song.objects.get(pk=pk)
    
    return render(request, 'song.html', {'song': music})

def albums(request):
    albums_list = Album.objects.filter(is_uploaded = True)
    return render(request, 'albums.html', {'albums_list':albums_list})

def album(request,pk):
    album = Album.objects.get(pk=pk)
    
    return render(request, 'album.html', {'album': album})

def singers(request):
    singers_list = Singer.objects.all()
    return render(request, 'singers.html', {'singers_list':singers_list})

def singer(request, singer):
    singer_albums = Album.objects.filter(singer=singer)

    return render(request, 'singer.html', {'singer_albums': singer_albums})


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
