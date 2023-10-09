from .models import *
from staff.models import *
from django import forms

class SongForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Название трека')
    song = forms.FileField(label='Файл трека')
    
    class Meta:
        model = Uploaded_Song
        fields = ['name', 'song']

class AlbumForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}),label='Название альбома')
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}),label='Описание альбома')
    singer = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}),label='Исполнитель')
    album_image = forms.ImageField(label='Изображение альбома')

    class Meta:
        model = Album
        fields = ['title','description','singer','album_image']

