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
    album_image = forms.ImageField(label='Изображение альбома')
    genre = forms.ChoiceField(choices=GENRES, required=True, label='Выберите жанр')

    class Meta:
        model = Album
        fields = ['title','description','album_image','genre']

class RateForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'textarea'}
    ), label='Отзыв об альбоме можно оставить здесь')
    rating = forms.ChoiceField(choices=RATE_CHOICES, required=True, label='Оцените альбом')

    class Meta:
        model = Album_review
        fields = ['text', 'rating']

    
