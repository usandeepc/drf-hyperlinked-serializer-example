from rest_framework.viewsets import ModelViewSet

from myapp.models import Album, Track, Artist
from myapp.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer    # noqa: E501

# Create your views here.


class track(ModelViewSet):
    serializer_class = TrackSerializer
    queryset = Track.objects.all()


class album(ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


class artist(ModelViewSet):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()
