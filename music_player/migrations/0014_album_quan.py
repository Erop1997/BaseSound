# Generated by Django 4.1.7 on 2023-10-09 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0013_remove_singer_album_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='quan',
            field=models.ManyToManyField(related_name='quan', to='music_player.singer'),
        ),
    ]
