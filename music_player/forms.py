from .models import *
from django import forms

class SongForm (forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}
    ), label='Название трека')
    
    singer = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'input'}
    ), label='Исполнитель')

    song = forms.FileField(label='Файл трека')
    song_image = forms.ImageField(label='Обложка трека', required=False)
    
    class Meta:
        model = Song
        fields = ['name', 'song', 'song_image', 'singer']