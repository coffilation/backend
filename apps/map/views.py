from rest_framework import mixins
from rest_framework import viewsets

from apps.map.filters import MapPlaceFilterSet
from apps.places.models import Place
from apps.places.serializers import PlaceSerializer


class MapPlaceViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    filterset_class = MapPlaceFilterSet
