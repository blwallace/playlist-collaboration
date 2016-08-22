from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Song(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey('auth.User')
    uri = models.CharField(max_length=100)
    playlist = models.ForeignKey('Playlist')
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return "/song/%i/" % self.id

    def __str__(self):
        return self.name


class Playlist(models.Model):
    # user = models.ForeignKey('auth.User')
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return "/playlist/%i/" % self.id

    def __str__(self):
        return self.name