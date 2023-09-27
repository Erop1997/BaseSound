from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from staff.models import *
from django.db.models import Q

from .forms import *

@login_required(login_url='/users/sign_in')
def home(request):
    new_songs = list(reversed(Song.objects.all()))
    popular_songs = Song.objects.order_by('-add_my')
    length = len(new_songs)-1
    return render(request, 'home.html', {'new_songs':new_songs, 'popular_songs':popular_songs, 'length':length})


def added(request,pk):
    song_data = Song.objects.get(pk=pk)
    song_data.add_my.add(request.user) if request.user not in song_data.add_my.all() \
        else song_data.add_my.remove(request.user)


def favorite(request):
    add_to = request.GET.get('add_to')
    favorite = Song.objects.filter(add_my=request.user)
    if add_to:
        added(request,add_to)
        return redirect('music_player:favorite')
    return render(request, 'favorite.html', {'favorite': favorite})

@login_required(login_url='/users/sign_in')
def songs(request):
    songs_list = Song.objects.all()
    add_to = request.GET.get('add_to')

    if add_to:
        added(request,add_to)
        return redirect('music_player:songs')
    
    return render(request, 'songs.html', {'songs_list':songs_list})

@login_required(login_url='/users/sign_in')
def song(request,pk):
    music = Song.objects.get(pk=pk)
    
    return render(request, 'song.html', {'song': music})


@login_required(login_url='/users/sign_in')
def albums(request):
    singer_pk = request.GET.get('singer_pk')
    albums_list = Album.objects.filter(is_uploaded = True)
    albums_list = albums_list.filter(album_singer=singer_pk) if singer_pk else albums_list
    return render(request, 'albums.html', {'albums_list':albums_list})

@login_required(login_url='/users/sign_in')
def album(request,pk):
    album = Album.objects.get(pk=pk)
    list_playlist = []

    for song in album.songs.all():
        playlist = {}
        playlist['title'] = f'{song.name}'
        playlist['file'] = f'/media/{song.song}'
        playlist['poster'] = f'/media/{song.album.album_image}'
        list_playlist.append(playlist)

    return render(request, 'album.html', {'album': album, 'list_playlist':list_playlist})

@login_required(login_url='/users/sign_in')
def singers(request):
    singers_list = Singer.objects.all()
    return render(request, 'singers.html', {'singers_list':singers_list})



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

@login_required(login_url='/users/sign_in')
def choosing_album(request):
    albums = Album.objects.filter(is_uploaded=True)
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and album_form.is_valid():
        album_form.save()
        created_album = Album.objects.last()
        return redirect('music_player:upload', pk=created_album.pk )
    
    return render(request, 'choosing_album.html', {'albums':albums, 'album_form': album_form})

def playlists(request):
    modal_selection = request.GET.get('modals')
    playlist_name = request.GET.get('playlist_name')
    
    if playlist_name:
        playlist = Playlist.objects.create(playlist_title=playlist_name, user=request.user)
        return redirect('music_player:playlist_creation', pk=playlist.pk)


    playlists = Playlist.objects.filter(user=request.user)
    modal = False 
    modal = True if modal_selection else modal
    return render(request, 'playlists.html', {'playlists':playlists,'modal':modal})

def playlist(request, pk):
    playlist = Playlist.objects.get(pk=pk)
    playlist_songs = []
    for song in playlist.songs.all():
        songs = {}
        songs['title'] = f'{song.name}'
        songs['file'] = f'/media/{song.song}'
        songs['poster'] = f'/media/{song.album.album_image}'
        playlist_songs.append(songs)
    return render(request, 'playlist.html', {'playlist':playlist,'playlist_songs':playlist_songs})

def playlist_creation(request,pk):
    playlist = Playlist.objects.get(pk=pk)
    return render(request, 'playlist_creation.html',{'playlist':playlist})