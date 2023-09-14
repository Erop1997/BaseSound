from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import os
from .models import *
from staff.models import *
from .forms import *


def home(request):
    albums = request.GET.get('albums')
    songs = Song.objects.all()

    songs = Song.objects.filter(album=albums) if albums else songs
    return render(request, 'home.html', {'songs':songs})

def song(request,pk):
    music = Song.objects.get(pk=pk)
    
    return render(request, 'song.html', {'song': music})


@login_required(login_url='/users/sign_in')
def upload(request, pk):


    form = SongForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        album = Album.objects.filter(pk=pk)
        instance.album = Uploaded_Album.objects.get_or_create(pk=album.pk)
        instance.save()
        return redirect('music_player:home')
    return render(request, 'upload.html', {'form': form})

def choosing_album(request):
    albums = Album.objects.all()
    album_form = AlbumForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and album_form.is_valid():
        album_form.save()
        created_album = Uploaded_Album.objects.last()
        return redirect(f'music_player:upload', pk=created_album.pk )
    
    return render(request, 'choosing_album.html', {'albums':albums, 'album_form': album_form})
