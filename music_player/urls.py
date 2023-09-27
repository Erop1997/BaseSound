from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home , name='home'),
    path('songs', views.songs , name='songs'),
    path('song/<int:pk>', views.song , name='song'),
    path('albums', views.albums , name='albums'),
    path('album/<int:pk>', views.album , name='album'),
    path('singers', views.singers , name='singers'),
    path('singer/<int:pk>', views.singer , name='singer'),
    path('upload/<int:pk>', views.upload , name='upload'),
    path('choosing_album/', views.choosing_album , name='choosing_album'),
    path('added/<int:pk>', views.added, name='added'),
    path('playlists', views.playlists, name='playlists'),
    path('playlist/<int:pk>', views.playlist, name='playlist'),
    path('favorite/', views.favorite, name='favorite')
]