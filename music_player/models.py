from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(default='ATL.jpeg')
    
    def __str__(self):
        return self.title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')
    name = models.CharField(max_length=255)
    song = models.FileField()

    def __str__(self):
        return self.name
    
