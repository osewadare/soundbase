import django_filters
from .models import Song

class Songfilter(django_filters.FilterSet):
    class Meta:
        model = Song
        fields = ['song_title']