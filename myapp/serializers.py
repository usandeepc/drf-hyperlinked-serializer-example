from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from myapp.models import Album, Artist, Track


class TrackSerializer(ModelSerializer):

    class Meta:
        model = Track
        fields = "__all__"


class AlbumSerializer(ModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )

    class Meta:
        model = Album
        fields = ['album_name', 'artist', 'tracks']


class ArtistSerializer(ModelSerializer):
    albums = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='album-detail'
    )

    class Meta:
        model = Artist
        fields = ['artist_name', 'artist_language', 'albums']
