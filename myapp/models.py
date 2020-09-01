from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=15)
    artist_language = models.CharField(max_length=10)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    album_name = models.CharField(max_length=20)
    language = models.CharField(max_length=7)
    artist = models.ForeignKey(
        Artist, related_name="albums", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.album_name


class Track(models.Model):
    track_name = models.CharField(max_length=20)
    track_order = models.IntegerField()
    album = models.ForeignKey(
        Album, related_name="tracks", on_delete=models.CASCADE
    )
    duration = models.IntegerField()

    def __str__(self):
        return self.track_name


class Production_company(models.Model):
    name = models.CharField(max_length=64)
    addr = models.CharField(max_length=64)
