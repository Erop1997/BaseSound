from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from staff.models import *
from django.db.models import Q, Count, Count
import ast

from .forms import *

@login_required(login_url='/users/sign_in')
def home(request):
    new_songs = list(reversed(Song.objects.all()))
    popular_songs = Song.objects.order_by('-views')
    length = len(new_songs)-1 if len(new_songs) < 4 else 4
    return render(request, 'home.html', {'new_songs':new_songs, 'popular_songs':popular_songs, 'length':length})

@login_required(login_url='/users/sign_in')
def added(request,pk):
    song_data = Song.objects.get(pk=pk)
     
    if request.user not in song_data.add_my.all():
        song_data.add_my.add(request.user)
        messages.success(request, 'Добавлено в мою музыку') 
    else:
        song_data.add_my.remove(request.user)
        messages.success(request, 'Удалено из моей музыки')
    
@login_required(login_url='/users/sign_in')
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
    actions = request.GET.get('actions')
    filter_for_genre = request.GET.get('filter_for_genre')
    genres = [i[0] for i in GENRES]
 

    if search:
        songs_list = Song.objects.filter(
            Q(name__icontains = search)
        )

    if add_to:
        added(request,add_to)
        return redirect('music_player:songs')
    
    if filter_for_genre:
        albums = Album.objects.filter(genre=filter_for_genre)
        songs_list = []
        for album in albums:
            for song in album.songs.all():
                songs_list.append(song)

    match actions:
        case 'for_views':
            songs_list = songs_list.order_by('-views')
        case 'for_likes':
            songs_list = filtering(songs_list, actions)
        case 'for_dislikes':
            songs_list = filtering(songs_list, actions)
    
    return render(request, 'songs.html', {'songs_list':songs_list, 'genres':genres})

@login_required(login_url='/users/sign_in')
def song(request,pk):
    music = Song.objects.get(pk=pk)
    music.views += 1
    music.save()

    return render(request, 'song.html', {'song': music})

@login_required(login_url='/users/sign_in')
def like(request, pk):
    music = Song.objects.get(pk=pk)
    if request.user not in music.likes.all():
        music.likes.add(request.user)
        music.dislikes.remove(request.user)
    elif request.user in music.likes.all():
        music.likes.remove(request.user)
    return redirect('music_player:song', pk=pk)    
    
@login_required(login_url='/users/sign_in')
def dislike(request, pk):
    music = Song.objects.get(pk=pk)
    if request.user not in music.dislikes.all():
        music.dislikes.add(request.user)
        music.likes.remove(request.user)
    elif request.user in music.dislikes.all():
        music.dislikes.remove(request.user)
    return redirect('music_player:song', pk=pk)        


@login_required(login_url='/users/sign_in')
def albums(request):
    singer_pk = request.GET.get('singer_pk')
    albums_list = Album.objects.filter(is_uploaded = True)
    albums_list = albums_list.filter(album_singer=singer_pk) if singer_pk else albums_list
    search = request.GET.get('search')
    actions = request.GET.get('actions')

    match actions:
        case 'for_views':
            albums_list = filtering(albums_list, actions)
        case 'for_tracks':
            albums_list = filtering(albums_list, actions)
        case 'for_rate':
            albums_list = filtering(albums_list, actions)

    if search:
        albums_list = Album.objects.filter(
            Q(title__icontains = search)
        )

    return render(request, 'albums.html', {'albums_list':albums_list})

def filtering(albums_list, action):
    alb_dict = {}
    match action:
        case 'for_views':
            for i in albums_list:
                alb_dict[i] = i.views_count()
        case 'for_tracks':
            for i in albums_list:
                alb_dict[i] = i.songs_count()
        case 'for_rate':
            for i in albums_list:
                alb_dict[i] = i.rate()
        case 'for_likes':
            for i in albums_list:
                alb_dict[i] = i.likes_counter()
        case 'for_dislikes':
            for i in albums_list:
                alb_dict[i] = i.dislikes_counter()
    sorted_list = []

    views = sorted(alb_dict.values(), reverse=True)

    while len(sorted_list) != len(albums_list):
        for i in alb_dict.keys():
            if views:
                if alb_dict[i] == views[0]:
                    sorted_list.append(i)
                    views.remove(views[0])
    albums_list = sorted_list
    return albums_list

@login_required(login_url='/users/sign_in')
def album(request,pk):
    album = Album.objects.get(pk=pk)
    reviews = Album_review.objects.filter(album=album)

    list_playlist = []

    for song in album.songs.all():
        playlist = {}
        playlist['title'] = f'{song.name}'
        playlist['file'] = f'/media/{song.song}'
        playlist['poster'] = f'/media/{song.album.album_image}'
        list_playlist.append(playlist)
        song.views += 1
        song.save()

    form = RateForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.listener = request.user
        instance.album = album
        instance.save()
        return redirect('music_player:album', pk=album.pk)
    
    return render(request, 'album.html', {'album': album, 'list_playlist':list_playlist, 'form':form, 'reviews':reviews})

@login_required(login_url='/users/sign_in')
def singers(request):
    singers_list = Singer.objects.all()
    search = request.GET.get('search')
    subscribe = request.GET.get('subscribe')

    if search:
        singers_list = Singer.objects.filter(
            Q(singer_name__icontains = search)
        )

    if subscribe:
        singer = Singer.objects.get(pk=subscribe)
        singer.subscribers.add(request.user) if request.user not in singer.subscribers.all() else singer.subscribers.remove(request.user)
        return redirect('music_player:singers')


    return render(request, 'singers.html', {'singers_list':singers_list})



@login_required(login_url='/users/sign_in')
def upload(request, pk):
    form = SongForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        album = Album.objects.get(pk=pk)
        instance.album = album
        instance.song_singer = album.album_singer
        instance.creator = request.user
        instance.save()
        messages.success(request, 'Отправлено на модерацию')
        return redirect('music_player:home')
    return render(request, 'upload.html', {'form': form})

@login_required(login_url='/users/sign_in')
def choosing_album(request):
    modal = True
    singer_name = request.GET.get('singer_name')
    singer_image = request.GET.get('singer_image')
    

    if singer_name and singer_image:
        modal = False
    singer = Singer.objects.filter(singer_name=singer_name)
    if singer:
        albums = Album.objects.filter(album_singer=singer[0], is_uploaded=True)
    else:
        albums = None
    album_form = AlbumForm(request.POST or None, request.FILES or None)

    
    if request.method == 'POST' and album_form.is_valid():
        singer_data = Singer.objects.filter(singer_name__icontains=singer_name)
        if not singer_data:
            Singer.objects.create(singer_name=singer_name, singer_image = singer_image)
            singer_data = Singer.objects.filter(singer_name=singer_name)
        album_form.save()
        created_album = Album.objects.last()
        singer_data[0].album.add(created_album)
        created_album.album_singer = singer_data[0]
        created_album.creator = request.user
        created_album.save()
        return redirect('music_player:upload', pk=created_album.pk )
    
    return render(request, 'choosing_album.html', {'albums':albums, 'album_form': album_form, 'modal':modal})

@login_required(login_url='/users/sign_in')
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

@login_required(login_url='/users/sign_in')
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

@login_required(login_url='/users/sign_in')
def playlist_creation(request,pk):
    adding = request.GET.get('adding')
    
    playlist = Playlist.objects.get(pk=pk)



    if adding:
        song = Song.objects.get(pk=adding)
        playlist.songs.add(song) if song not in playlist.songs.all() else playlist.songs.remove(song)
        return redirect('music_player:playlist_creation', pk=playlist.pk)

        
    songs = [i for i in Song.objects.all() if i not in playlist.songs.all()]
    return render(request, 'playlist_creation.html',{'playlist':playlist, 'songs':songs,})

@login_required(login_url='/users/sign_in')
def delete_notify(request, pk, object, path):
    match object:
        case 'song':
            song = Song.objects.get(pk=pk)
            notify_obj = Notification_object.objects.get(notify_song = song)
            notify_obj.notify_song.remove(song)
            song.is_new = False
            song.save()
        case 'album':
            album = Album.objects.get(pk=pk)
            notify_obj = Notification_object.objects.get(notify_album = album)
            notify_obj.notify_album.remove(album)
            album.is_new = False
            album.save()
        case 'del_track':
            notify_obj = Notification_object.objects.get(notify = Notificaton.objects.get(notify_user = request.user))
            thing = "{}'track':'{}'{};".format('{',pk,'}')
            notify_obj.deleted_things = notify_obj.deleted_things.replace(thing,'')
            notify_obj.save()
        case 'del_album':
            notify_obj = Notification_object.objects.get(notify = Notificaton.objects.get(notify_user = request.user))
            thing = "{}'album':'{}'{};".format('{',pk,'}')
            notify_obj.deleted_things = notify_obj.deleted_things.replace(thing,'')
            notify_obj.save()
    path = path.split('.')
    if len(path) > 2:
        pk = path[2]
        path = f'{path[0]}:{path[1]}'
        return redirect(path, pk=pk)
    path = f'{path[0]}:{path[1]}'
    return redirect(path)

def playlist_name_image(request):
    value = request.GET.get('value')
    
    playlist_form = PlaylistCreationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and playlist_form.is_valid():
        instance = playlist_form.save(commit=False)
        instance.user = request.user
        instance.save()
        playlist = Playlist.objects.last()
        return redirect('music_player:playlist_creation', pk=playlist.pk)

    return render(request, 'playlist_name_image.html', {'playlist_form':playlist_form})