# Generated by Django 4.2.4 on 2023-09-18 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_player', '0011_uploaded_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='chosen',
            field=models.BooleanField(default=False),
        ),
    ]