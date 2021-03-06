# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-30 15:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='slug', unique=True)),
                ('artiste', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('release_year', models.CharField(max_length=4)),
                ('rating', models.CharField(choices=[('1 STAR', '1 STAR'), ('2 STAR', '2 STAR'), ('3 STAR', '3 STAR'), ('4 STAR', '4 STAR'), ('5 STAR', '5 STAR')], default='1 STAR', max_length=6)),
                ('album_art', models.FileField(upload_to='album_art')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=100)),
                ('slug', models.SlugField(default='slug', unique=True)),
                ('artiste', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('release_year', models.CharField(max_length=4)),
                ('rating', models.CharField(choices=[('1 STAR', '1 STAR'), ('2 STAR', '2 STAR'), ('3 STAR', '3 STAR'), ('4 STAR', '4 STAR'), ('5 STAR', '5 STAR')], default='1 STAR', max_length=6)),
                ('song_file', models.FileField(upload_to='songs')),
                ('song_art', models.FileField(upload_to='song_art')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicplay.Album')),
            ],
        ),
    ]
