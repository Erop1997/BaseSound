# Generated by Django 4.1.7 on 2023-10-16 17:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_player', '0006_merge_0003_album_review_0005_album_is_new_song_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='dislikes',
            field=models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
    ]