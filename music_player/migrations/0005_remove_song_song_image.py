# Generated by Django 4.2.4 on 2023-09-11 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0004_song_singer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='song_image',
        ),
    ]