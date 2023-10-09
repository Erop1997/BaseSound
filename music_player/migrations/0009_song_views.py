# Generated by Django 4.1.7 on 2023-10-05 14:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_player', '0008_playlist_playlist_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='views',
            field=models.ManyToManyField(related_name='song_views', to=settings.AUTH_USER_MODEL),
        ),
    ]