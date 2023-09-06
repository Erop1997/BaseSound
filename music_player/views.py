from django.shortcuts import render
import os
from .models import *
# Create your views here.
def home(request):
    songs = Song.objects.all()
    return render(request, 'home.html', {'songs':songs})

def song(request):
    music = Song.objects.get(name='Monolit')
    print(music.album.image)
    return render(request, 'song.html', {'song': music})