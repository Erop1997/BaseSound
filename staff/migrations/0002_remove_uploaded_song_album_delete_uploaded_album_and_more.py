# Generated by Django 4.1.7 on 2023-09-15 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaded_song',
            name='album',
        ),
        migrations.DeleteModel(
            name='Uploaded_Album',
        ),
        migrations.DeleteModel(
            name='Uploaded_Song',
        ),
    ]
