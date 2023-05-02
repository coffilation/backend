from drf_spectacular.utils import OpenApiParameter, extend_schema, extend_schema_view
from rest_framework import mixins
from rest_framework import viewsets

from apps.map.filters import MapPlacesFilterSet
from apps.map.serializers import MapPlacesQuerySerializer
from apps.places.models import Place
from apps.places.serializers import PlaceSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[MapPlacesQuerySerializer, OpenApiParameter(
            'viewbox',
            description='`x1,y1,x2,y2`\n\n`x` is longitude, `y` is latitude',
            default='29.608218,60.049997,30.694038,59.760964',
            required=True,
        )], responses=PlaceSerializer
    )
)
class MapPlacesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    pagination_class = None
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    filterset_class = MapPlacesFilterSet

    def list(self, request, *args, **kwargs):
        MapPlacesQuerySerializer(data=request.query_params).is_valid(raise_exception=True)
        return super().list(request, *args, **kwargs)
