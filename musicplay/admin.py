from django.contrib import admin
from .models import *


class SongAdmin(admin.ModelAdmin):
    list_display = ['song_title','artiste', 'genre', 'song_file', 'song_art']
    search_fields = ['song_title']
    prepopulated_fields = {'slug': ('song_title',)}

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_title','artiste', 'genre', 'album_art']
    search_fields = ['album_title']
    prepopulated_fields = {'slug': ('album_title',)}

admin.site.register(Song, SongAdmin)
admin.site.register(Album, AlbumAdmin)
