from django import forms

from .models import Song, Playlist

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ('uri','name',)

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ('name',)