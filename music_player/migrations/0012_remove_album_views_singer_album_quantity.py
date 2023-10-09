# Generated by Django 4.1.7 on 2023-10-09 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0011_remove_singer_singer_views_remove_singer_songs_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='views',
        ),
        migrations.AddField(
            model_name='singer',
            name='album_quantity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='album_quantity', to='music_player.album'),
        ),
    ]