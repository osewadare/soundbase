from django.conf.urls import url
from . import views

app_name = 'musicplay'

urlpatterns = [

    url(r'^$', views.indexview, name='index'),
    url(r'^albums$', views.albumsview, name='albums'),
    url(r'^song/(?P<pk>[0-9]+)/$', views.SongDetailView.as_view(), name='songdetail'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetailView, name='albumdetail'),
    url(r'song/add/$', views.SongCreate.as_view(), name='add_song'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='add_album'),
    url(r'song/(?P<pk>[0-9]+)/update/$', views.SongUpdate.as_view(), name='song_update'),
    url(r'song/(?P<pk>[0-9]+)/delete/$', views.SongDelete.as_view(), name='song_delete'),
    url(r'album/(?P<pk>[0-9]+)/update/$', views.AlbumUpdate.as_view(), name='album_update'),
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),
    url(r'^search/$', views.search, name='search'),
    url(r'^api/songs/$', views.songs_list_api.as_view(), name='songlistapi'),
    url(r'^api/songs/(?P<pk>[0-9]+)/$', views.songs_detail_api.as_view(), name='songdetailapi')
]