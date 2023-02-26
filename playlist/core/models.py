from django.db import models


class Song(models.Model):
    name = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    duration = models.IntegerField(min=1)

    class Meta:
        ordering = ["-artist"]

    def __str__(self) -> str:
        return f'{self.artist} - {self.name}'


class Playlist(models.Model):
    name = models.CharField(max_length=150)
    songs = models.ManyToManyField(Song, through=PlaylistsSongs)


class PlaylistsSongs(models.Model):
    song = models.ForeignKey(
        Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(
        Playlist, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-playlist"]
        constraints = [
            models.UniqueConstraint(
                fields=["song", "playlist"], name="unique playlist song"
            )
        ]

    def __str__(self):
        return f'{self.config} {self.key_value}'
