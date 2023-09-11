from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    album_image = models.ImageField(default='ATL.jpeg')
    
    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()
    singer = models.CharField(max_length=255)

    def __str__(self):
        return self.name
