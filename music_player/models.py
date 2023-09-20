from django.db import models
from django.contrib.auth.models import User
from . import *

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    album_image = models.ImageField(default='ATL.jpeg')
    is_uploaded = models.BooleanField(default=False)
    album_singer = models.ForeignKey('music_player.Singer',related_name='album_singer', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        if len(self.songs.all()) > 1 or len(self.uploaded_songs.all()) > 1:
            return self.title
        else:
            return f'{self.title} - Single'


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()
    add_my = models.ManyToManyField(User, related_name='my_songs', blank=True)
    song_singer = models.ForeignKey('music_player.Singer', related_name='song_singer' ,on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

class Singer(models.Model):
    singer_name = models.CharField(max_length=255)
    album = models.ManyToManyField(Album, related_name='singer', blank=True)
    songs = models.ManyToManyField(Song, related_name='singer', blank=True)
    singer_image = models.ImageField(default='6120361940.jpg')

    def __str__(self):
        return self.singer_name

class Uploaded_Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='uploaded_songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()
    chosen = models.BooleanField(default=False)

    def __str__(self):
        return self.name