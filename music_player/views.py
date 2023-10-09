from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from staff.models import *
from django.db.models import Q

from .forms import *

@login_required(login_url='/users/sign_in')
def home(request):
    new_songs = list(reversed(Song.objects.all()))
    popular_songs = Song.objects.order_by('-add_my')
    length = len(new_songs)-1 if len(new_songs) < 4 else 4

    return render(request, 'home.html', {'new_songs':new_songs, 'popular_songs':popular_songs, 'length':length})


def added(request,pk):
    song_data = Song.objects.get(pk=pk)
     
    if request.user not in song_data.add_my.all():
        song_data.add_my.add(request.user)
        messages.success(request, 'Добавлено в мою музыку') 
    else:
        song_data.add_my.remove(request.user)
        messages.success(request, 'Удалено из моей музыки')
    

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
    search = request.GET.get('search')

    if search:
        songs_list = Song.objects.filter(
            Q(name__icontains = search)
        )

    if add_to:
        added(request,add_to)
        return redirect('music_player:songs')
    
    return render(request, 'songs.html', {'songs_list':songs_list})

@login_required(login_url='/users/sign_in')
def song(request,pk):
    music = Song.objects.get(pk=pk)
    if request.user not in music.views.all():
        music.views.add(request.user)
    
    return render(request, 'song.html', {'song': music})


@login_required(login_url='/users/sign_in')
def albums(request):
    singer_pk = request.GET.get('singer_pk')
    albums_list = Album.objects.filter(is_uploaded = True)
    albums_list = albums_list.filter(album_singer=singer_pk) if singer_pk else albums_list
    search = request.GET.get('search')

    if search:
        albums_list = Album.objects.filter(
            Q(title__icontains = search)
        )

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
    search = request.GET.get('search')

    if search:
        singers_list = Singer.objects.filter(
            Q(singer_name__icontains = search)
        )

    return render(request, 'singers.html', {'singers_list':singers_list})



@login_required(login_url='/users/sign_in')
def upload(request, pk):
    form = SongForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        album = Album.objects.get(pk=pk)
        instance.album = album
        instance.song_singer = album.album_singer
        instance.save()
        messages.success(request, 'Отправлено на модерацию')
        return redirect('music_player:home')
    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/users/sign_in')
def choosing_album(request):
    albums = Album.objects.filter(is_uploaded=True)
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and album_form.is_valid():
        singer = album_form.data.get('singer')
        singer_data = Singer.objects.filter(singer_name__icontains=singer)
        if not singer_data:
            Singer.objects.create(singer_name=singer)
            singer_data = Singer.objects.filter(singer_name=singer)
        album_form.save()
        created_album = Album.objects.last()
        singer_data[0].album.add(created_album)
        created_album.album_singer = singer_data[0]
        created_album.save()
        return redirect('music_player:upload', pk=created_album.pk )
    
    return render(request, 'choosing_album.html', {'albums':albums, 'album_form': album_form})

def playlists(request):
    modal_selection = request.GET.get('modals')
    playlist_name = request.GET.get('playlist_name')
    playlist_image = request.GET.get('playlist_image')
    
    if playlist_name:
        playlist = Playlist.objects.create(playlist_title=playlist_name,playlist_image=playlist_image, user=request.user)

        return redirect('music_player:playlist_creation', pk=playlist.pk)


    playlists = Playlist.objects.filter(user=request.user)
    modal = False 
    modal = True if modal_selection else modal
    return render(request, 'playlists.html', {'playlists':playlists,'modal':modal})

def playlist(request, pk):
    action = request.GET.get('action')
    playlist = Playlist.objects.get(pk=pk)

    if action:
        playlist.delete()
        return redirect('music_player:playlists')
    
    playlist_songs = []
    for song in playlist.songs.all():
        songs = {}
        songs['title'] = f'{song.name}'
        songs['file'] = f'/media/{song.song}'
        songs['poster'] = f'/media/{playlist.playlist_image}'
        playlist_songs.append(songs)
    return render(request, 'playlist.html', {'playlist':playlist,'playlist_songs':playlist_songs})

def playlist_creation(request,pk):
    adding = request.GET.get('adding')
    
    playlist_name = request.GET.get('playlist_name')
    playlist = Playlist.objects.get(pk=pk)

    if playlist_name:
        playlist.playlist_title = playlist_name
        playlist.save()
        return redirect('music_player:playlist_creation', pk=playlist.pk)

    modal = False
    modals = request.GET.get('modals')
    if modals:
        modal = True

    if adding:
        song = Song.objects.get(pk=adding)
        playlist.songs.add(song) if song not in playlist.songs.all() else playlist.songs.remove(song)
        return redirect('music_player:playlist_creation', pk=playlist.pk)

        
    songs = [i for i in Song.objects.all() if i not in playlist.songs.all()]
    return render(request, 'playlist_creation.html',{'playlist':playlist, 'songs':songs, 'modal':modal})
