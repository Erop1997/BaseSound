from django.shortcuts import render,redirect
from music_player.models import *

def admin(request):
    action = request.GET.get('action')
    pk = request.GET.get('pk')

    if action:
        actions(action, pk)
        return redirect('staff:admin')

    uploaded_albums = Album.objects.filter(is_uploaded=False)
    uploaded_tracks = Uploaded_Song.objects.all()


    return render(request, 'admin.html', {'uploaded_albums': uploaded_albums, 'uploaded_tracks': uploaded_tracks})


def add_album(request, pk):
    
    return render(request, 'add_album.html')

def actions(action, pk):
    match action:
        case 'add_track':
            track = Uploaded_Song.objects.get(pk=pk)
            Song.objects.create(name = track.name, song = track.song, album = track.album)
            track.delete()
        case 'delete_track':
            Uploaded_Song.objects.get(pk=pk).delete()
        case 'delete_album':
            Album.objects.get(pk=pk).delete()