# Generated by Django 4.1.7 on 2023-09-03 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0007_alter_song_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='song',
            field=models.FileField(upload_to=''),
        ),
    ]
