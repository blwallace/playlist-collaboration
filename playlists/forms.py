from django import forms

from .models import Song, Playlist

class SongForm(forms.ModelForm):

    playlist = forms.ModelChoiceField(queryset=Playlist.objects.all())

    class Meta:
        model = Song
        fields = ('uri','name','playlist')

class PlaylistForm(forms.ModelForm):

    class Meta:
        model = Playlist
        fields = ('name',)