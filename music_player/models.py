from django.db import models

class Song(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(default='ATL.jpeg')
    song = models.FileField()

    def __str__(self):
        return self.name