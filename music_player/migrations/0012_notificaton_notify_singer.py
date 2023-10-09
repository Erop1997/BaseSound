# Generated by Django 4.2.4 on 2023-10-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0011_notificaton'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificaton',
            name='notify_singer',
            field=models.ManyToManyField(blank=True, related_name='notify_singer', to='music_player.singer'),
        ),
    ]
