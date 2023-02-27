from django.contrib import admin

from .models import Playlist, PlaylistsSong, Song

admin.site.register(Song)
admin.site.register(Playlist)
admin.site.register(PlaylistsSong)
