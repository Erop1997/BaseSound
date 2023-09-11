from .models import *
from django import forms

class SongForm (forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}
    ), label='Название трека')
    song = forms.FileField(label='Файл трека')
    song_image = forms.ImageField(label='Обложка трека', required=False)
    singer = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}
    ), label='Исполнитель')

    class Meta:
        model = Song
        fields = ['name', 'song', 'song_image', 'singer']