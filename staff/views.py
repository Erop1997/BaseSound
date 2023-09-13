from django.shortcuts import render
from music_player.models import Song, Album 

def home(request):
    songs = Song.objects.all()

    return render(request, 'admin.html', {songs:'songs'})


def song_select(request):
    pass
    return render(request, 'song_select.html')


