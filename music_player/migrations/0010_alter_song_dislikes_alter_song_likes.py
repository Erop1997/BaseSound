# Generated by Django 4.1.7 on 2023-10-19 11:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_player', '0009_alter_song_dislikes_alter_song_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
