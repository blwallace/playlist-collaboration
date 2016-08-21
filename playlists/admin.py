from django.contrib import admin
from .models import Song, Playlist

admin.site.register([Song,Playlist])
