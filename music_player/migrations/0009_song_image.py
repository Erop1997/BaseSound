# Generated by Django 4.1.7 on 2023-09-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0008_alter_song_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='image',
            field=models.ImageField(default='ATL.jpeg', upload_to=''),
        ),
    ]
