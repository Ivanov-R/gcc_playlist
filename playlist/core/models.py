from django.db import models


class Song(models.Model):
    artist = models.CharField(max_length=150)
    name = models.CharField(max_length=150)
    duration = models.IntegerField()

    class Meta:
        ordering = ["-artist"]

    def __str__(self) -> str:
        return f"{self.artist} - {self.name}"


class Playlist(models.Model):
    name = models.CharField(max_length=150)
    songs = models.ManyToManyField(Song, through="PlaylistsSong")

    def __str__(self) -> str:
        return f"{self.name}"


class PlaylistsSong(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    head = models.BooleanField()
    next = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="next_song",
    )
    previous = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="previous_song",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["song", "playlist"], name="unique playlist song"
            )
        ]

    def __str__(self):
        return f"{self.song} {self.playlist}"

    # def save(self, *args, **kwargs):
    #     if self.head:
    #         try:
    #             temp = PlaylistsSong.objects.filter(
    #                 head=True, playlist=Playlist
    #             ).first()
    #             if self != temp:
    #                 temp.head = False
    #                 temp.save()
    #         except PlaylistsSong.DoesNotExist:
    #             pass
    #     super(PlaylistsSong, self).save(*args, **kwargs)
