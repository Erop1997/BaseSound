# Generated by Django 4.2.4 on 2023-10-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0007_uploaded_song_song_singer'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='playlist_image',
            field=models.ImageField(default='6120361940.jpg', upload_to=''),
        ),
    ]
