from django.shortcuts import render
import os
from .models import *


def home(request):
    albums = request.GET.get('albums')
    songs = Song.objects.all()

    songs = Song.objects.filter(album=albums) if albums else songs

    return render(request, 'home.html', {'songs':songs})

<<<<<<< HEAD

def song(request):
    music = Song.objects.get(name='Monolit')
=======
def song(request,pk):
    music = Song.objects.get(pk=pk)
>>>>>>> 634be568656fb55ffb14a9a1b1c5e141c338dbed
    return render(request, 'song.html', {'song': music})