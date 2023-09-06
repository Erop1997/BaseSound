from django.shortcuts import render
import os
from .models import *


def home(request):
    albums = request.GET.get('albums')
    songs = Song.objects.all()

    songs = Song.objects.filter(album=albums) if albums else songs

    return render(request, 'home.html', {'songs':songs})

def song(request,pk):
    music = Song.objects.get(pk=pk)
    return render(request, 'song.html', {'song': music})