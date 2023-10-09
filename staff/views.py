from django.shortcuts import render,redirect
from music_player.models import *

def admin(request):
    action = request.GET.get('action')
    pk = request.GET.get('pk')

    if action:
        actions(request, action, pk)
        return redirect('staff:admin')

    uploaded_albums = Album.objects.filter(is_uploaded=False)
    uploaded_tracks = Uploaded_Song.objects.all()


    return render(request, 'admin.html', {'uploaded_albums': uploaded_albums, 'uploaded_tracks': uploaded_tracks})


def add_album(request, pk):
    action = request.GET.get('action')
    primary_key = request.GET.get('pk')
    uploaded_album = Album.objects.get(pk=pk)
    uploaded_tracks = Uploaded_Song.objects.filter(album = uploaded_album)
    list_playlist = []
    

    if action == 'add_alb':
            uploaded_album = Album.objects.get(pk=pk)
            uploaded_album.is_uploaded = True
            uploaded_album.save()
            uploaded_songs = Uploaded_Song.objects.filter(album=uploaded_album)
            for song in uploaded_songs:
                Song.objects.create(name = song.name, song = song.song, album = song.album, song_singer = song.album.album_singer)
                song.delete()
            notify = Notificaton.objects.get(notify_user = request.user)
            notify.notify_album.add(uploaded_album)
            return redirect('staff:admin')
    elif action:
        actions(request, action, primary_key)
        return redirect('staff:add_album', pk=pk)

    for song in uploaded_tracks:
        playlist = {}
        playlist['title'] = f'{song.name}'
        playlist['file'] = f'/media/{song.song}'
        playlist['poster'] = f'/media/{song.album.album_image}'
        list_playlist.append(playlist)
    return render(request, 'add_album.html', {'uploaded_album':uploaded_album, 'uploaded_tracks':uploaded_tracks, 'list_playlist':list_playlist})

def actions(request, action, pk):
    match action:
        case 'add_track':
            uploaded_song = Uploaded_Song.objects.get(pk=pk)
            song = Song.objects.create(name = uploaded_song.name, song = uploaded_song.song, album = uploaded_song.album, song_singer = uploaded_song.album.album_singer)
            notify = Notificaton.objects.get(notify_user = request.user)
            notify.notify_song.add(song)
            uploaded_song.delete()
        case 'delete_track':
            uploaded_song = Uploaded_Song.objects.get(pk=pk)
            notify = Notificaton.objects.get(notify_user = request.user)
            notify.notify_song.add(uploaded_song)
            uploaded_song.delete()
        case 'delete_album':
            uploaded_album = Album.objects.get(pk=pk)
            notify = Notificaton.objects.get(notify_user = request.user)
            notify.notify_album.add(uploaded_album)
            uploaded_album.delete()
        case 'choose':
            uploaded_song = Uploaded_Song.objects.get(pk=pk)
            uploaded_song.chosen = True 
            uploaded_song.save()
        case 'unchoose':
            uploaded_song = Uploaded_Song.objects.get(pk=pk)
            uploaded_song.chosen = False
            uploaded_song.save()
        case 'choose_all':
            album = Album.objects.get(pk=pk)
            uploaded_song = Uploaded_Song.objects.filter(album=album)
            uploaded_song.update(chosen=True)
        case 'unchoose_all':
            album = Album.objects.get(pk=pk)
            uploaded_song = Uploaded_Song.objects.filter(album=album)
            uploaded_song.update(chosen=False)
