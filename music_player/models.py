from django.db import models
from django.contrib.auth.models import User
from . import *

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    album_image = models.ImageField(default='ATL.jpeg')
    is_uploaded = models.BooleanField(default=False)
    album_singer = models.ForeignKey('music_player.Singer',related_name='album_singer', on_delete=models.CASCADE, null=True, blank=True)
    creator = models.ForeignKey(User, related_name='albums', on_delete=models.CASCADE, blank=True, null=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        if len(self.songs.all()) > 1 or len(self.uploaded_songs.all()) > 1:
            return self.title
        else:
            return f'{self.title} - Single'
        
    def views_count(self):
        return sum([i.views for i in self.songs.all()])

RATE_CHOICES = [
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
    (7, '7'),
    (8, '8'),
    (9, '9'),
    (10, '10')
]

class album_review(models.Model):
    listener = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True)
    rating = models.PositiveSmallIntegerField(choices=RATE_CHOICES)

    def __str__(self):
        return f'{self.listener.username} об {self.album.title}'

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()
    add_my = models.ManyToManyField(User, related_name='my_songs', blank=True)
    song_singer = models.ForeignKey('music_player.Singer', related_name='song_singer' ,on_delete=models.CASCADE, null=True, blank=True)
    views = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    creator = models.ForeignKey(User, related_name='songs', on_delete=models.CASCADE, blank=True, null=True)
    is_new = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    
    


class Singer(models.Model):
    singer_name = models.CharField(max_length=255)
    album = models.ManyToManyField(Album, related_name='singer', blank=True)
    singer_image = models.ImageField(default='6120361940.jpg')
    subscribers = models.ManyToManyField(User, related_name='subscribers',blank=True)

    def __str__(self):
        return self.singer_name
    
    def views_count(self):
        return sum([i.views for i in self.song_singer.all()])

    def album_count(self):
        return len([i for i in self.album_singer.all()])        


class Uploaded_Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='uploaded_songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()
    chosen = models.BooleanField(default=False)
    song_singer = models.ForeignKey('music_player.Singer', related_name='uploaded_song_singer' ,on_delete=models.CASCADE, null=True, blank=True)
    creator = models.ForeignKey(User, related_name='uploaded_songs', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Playlist(models.Model):
    playlist_title = models.CharField(max_length=255)
    playlist_image = models.ImageField(default='6120361940.jpg')
    songs = models.ManyToManyField(Song, related_name='song_playlist')
    user = models.ForeignKey(User, related_name='user_playlist',on_delete=models.CASCADE)

    def __str__(self):
        return self.playlist_title
    
class Notificaton(models.Model):
    notify_user = models.ForeignKey(User, related_name='notify_user', on_delete=models.CASCADE)

    def __str__(self):
        return f'Нотификация юзера - {self.notify_user}'

class Notification_object(models.Model):
    notify = models.ForeignKey(Notificaton, related_name='notify', on_delete=models.CASCADE)
    notify_song = models.ManyToManyField(Song, related_name='notify_song', blank=True)
    notify_album = models.ManyToManyField(Album, related_name='notify_album', blank=True)
    notify_singer = models.ManyToManyField(Singer, related_name='notify_singer', blank=True)
    deleted_things = models.CharField(max_length=225,blank=True)

    def __str__(self):
        return f'Объекты нотификации - {self.notify}'
