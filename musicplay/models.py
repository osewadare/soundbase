from django.db import models
from django.core.urlresolvers import reverse

RATINGS_CHOICE = (('1 STAR','1 STAR'),('2 STAR','2 STAR'),('3 STAR','3 STAR'),('4 STAR','4 STAR'),('5 STAR','5 STAR'))

class Song(models.Model):
    song_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    artiste = models.CharField(max_length=100)
    album = models.ForeignKey('Album')
    genre = models.CharField(max_length=100)
    release_year = models.CharField(max_length=4)
    rating = models.CharField(max_length=6, choices=RATINGS_CHOICE, default='1 STAR' )
    song_file = models.FileField(upload_to='songs')
    song_art = models.FileField(upload_to='song_art')

    def get_absolute_url(self):
        return reverse('musicplay:songdetail', kwargs={'pk':self.pk})

    def __str__(self):
        return (self.song_title)

class Album (models.Model):
    album_title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    artiste = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    release_year = models.CharField(max_length=4)
    rating = models.CharField(max_length=6, choices=RATINGS_CHOICE, default='1 STAR')
    album_art = models.FileField(upload_to='album_art')

    def __str__(self):
        return (self.album_title)


    def get_absolute_url(self):
        return reverse('musicplay:albumdetail', kwargs={'pk':self.pk})

