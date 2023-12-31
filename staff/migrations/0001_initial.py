# Generated by Django 4.2.4 on 2023-09-13 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uploaded_Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('album_image', models.ImageField(default='ATL.jpeg', upload_to='')),
                ('singer', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Uploaded_Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('song', models.FileField(upload_to='')),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='staff.uploaded_album')),
            ],
        ),
    ]
