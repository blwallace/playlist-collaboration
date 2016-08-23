from django.shortcuts import render, get_object_or_404
from .models import Song, Playlist
from .forms import SongForm, PlaylistForm
from django.shortcuts import redirect
from django.utils import timezone


def song_list(request):
    """ Displays all songs for all users"""
    songs = Song.objects.all()
    return render(request, 'playlists/song_list.html', {'songs': songs})


def song_add(request):
    """ Adds a song.
        User Inputs: name, uri, playlist, created/published date"""
    if request.method == "POST":
        form = SongForm(request.POST)
        if form.is_valid():
            song = form.save(commit=False)
            song.playlist = Playlist.objects.get(name="Test Playlist")
            song.created_date = timezone.now()
            song.published_date = timezone.now()
            song.save()
            return redirect('song_detail', pk=song.pk)

    else:
        songs = Song.objects.all()
        form = SongForm()
        return render(request, 'playlists/form.html', {'songs': songs, 'form': form})


def song_detail(request, pk):
    """Displays data for a song"""
    song = get_object_or_404(Song, pk=pk)
    return render(request, 'playlists/song_detail.html', {'song': song})


def playlist_list(request):
    """ Displays all playlists for all users"""
    playlists = Playlist.objects.all()
    return render(request, 'playlists/playlist_list.html', {'playlists': playlists})


def playlist_detail(request, pk):
    """ Displays the details for a playlist"""
    playlist = get_object_or_404(Playlist, pk=pk)
    return render(request, 'playlists/playlist_detail.html', {'playlist': playlist})


def playlist_add(request):
    """Adds a playlist
        inputs: Name, created, published dates """
    if request.method == "POST":
        form = PlaylistForm(request.POST)
        if form.is_valid():
            playlist = form.save(commit=False)
            playlist.created_date = timezone.now()
            playlist.published_date = timezone.now()
            playlist.save()
            return redirect('playlist_detail', pk=playlist.pk)
    else:
        playlists = Playlist.objects.all()
        form = PlaylistForm()
        return render(request, 'playlists/form.html', {'playlists': playlists, 'form': form})