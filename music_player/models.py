from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    album_image = models.ImageField(default='ATL.jpeg')
    singer = models.CharField(max_length=255)
    
    def __str__(self):
        if len(self.songs.all()) > 1:
            return self.title
        else:
            return f'{self.title} - Single'
    
    


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs', null=True, blank=True)
    name = models.CharField(max_length=255)
    song = models.FileField()

    def __str__(self):
        return self.name
