from django.db import models
from django.contrib.auth.models import User

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    album_image = models.ImageField(default='ATL.jpeg')
    singer = models.CharField(max_length=255)
    is_uploaded = models.BooleanField(default=False)
    
    def __str__(self):
        if len(self.songs.all()) > 1 or len(self.uploaded_songs.all()) > 1:
            return self.title
        else:
            return f'{self.title} - Single'
    



class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()
    add_my = models.ManyToManyField(User, related_name='my_songs')

    def __str__(self):
        return self.name


class Uploaded_Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='uploaded_songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()

    def __str__(self):
        return self.name