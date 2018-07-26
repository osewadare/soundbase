from django.forms import ModelForm
from .models import *

class AddSongForm(ModelForm):
    class Meta:
        model = Song
        fields = ['song_title', 'artiste', 'album', 'genre', 'release_year', 'rating', 'song_file', 'song_art']

class AddAlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['album_title', 'artiste', 'genre', 'release_year', 'rating', 'album_art']
