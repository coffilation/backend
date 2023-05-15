from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework import viewsets

from apps.map.filters import MapPlacesFilterSet
from apps.places.models import Place
from apps.places.serializers import PlaceSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[OpenApiParameter(
            'viewbox',
            description='`x1,y1,x2,y2`\n\n`x` is longitude, `y` is latitude',
            default='29.608218,60.049997,30.694038,59.760964',
        )], responses=PlaceSerializer
    )
)
class MapPlacesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    filterset_class = MapPlacesFilterSet
