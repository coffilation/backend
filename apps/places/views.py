from functools import reduce
import requests
from django.db.models import Q
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.response import Response
from dots.settings.base import NOMINATIM_LOOKUP_ENDPOINT, NOMINATIM_SEARCH_ENDPOINT, REST_FRAMEWORK
from .serializers import *
from rest_framework import status, viewsets, mixins
from rest_framework.decorators import action

from .enums import OSM_TYPE__TO_PREFIX


class PlaceViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    filterset_fields = ['compilation']


class NominatimPlaceViewSet(viewsets.GenericViewSet):
    pagination_class = None

    nominatim_request_params = {
        'limit': REST_FRAMEWORK['PAGE_SIZE'],
        'format': 'jsonv2',
        'addressdetails': 1,
        'accept-language': 'ru',
    }

    @extend_schema(parameters=[NominatimLookupQuerySerializer], responses=PlaceSerializer)
    @action(detail=False, methods=['get'])
    def lookup(self, request):
        serializer = NominatimLookupQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        if Place.objects.filter(**serializer.data).exists():
            return Response(PlaceSerializer(Place.objects.get(**serializer.data)).data)

        try:
            lookup_data = requests.get(
                NOMINATIM_LOOKUP_ENDPOINT,
                params={
                    **self.nominatim_request_params,
                    'osm_ids': OSM_TYPE__TO_PREFIX[serializer.data['osm_type']] + str(
                        serializer.data['osm_id']
                    )
                },
            ).json()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_424_FAILED_DEPENDENCY)

        for place in lookup_data:
            if place['category'] == serializer.data['category']:
                place_serializer = PlaceSerializer(data=place)
                place_serializer.is_valid(raise_exception=True)
                place_serializer.save()
                return Response(place_serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        parameters=[NominatimSearchQuerySerializer, OpenApiParameter(
            'viewbox',
            description='`x1,y1,x2,y2`\n\n`x` is longitude, `y` is latitude',
            default='29.608218,60.049997,30.694038,59.760964',
            required=True,
        )],
        responses=PlaceSerializer(many=True)
    )
    @action(detail=False, methods=['get'])
    def search(self, request):
        serializer = NominatimSearchQuerySerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)

        try:
            search_data = requests.get(
                NOMINATIM_SEARCH_ENDPOINT,
                params={
                    **self.nominatim_request_params,
                    'bounded': 1,
                    **serializer.data,
                }
            ).json()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_424_FAILED_DEPENDENCY)

        queryset = Place.objects.none()

        if search_data:
            place_serializer = PlaceSerializer(data=search_data, many=True)
            place_serializer.is_valid(raise_exception=True)

            Place.objects.bulk_create(
                [Place(**place_data) for place_data in place_serializer.validated_data],
                ignore_conflicts=True
            )

            place_query = reduce(
                lambda query, place: query | Q(
                    osm_id=place['osm_id'],
                    osm_type=place['osm_type'],
                    category=place['category'],
                ),
                search_data,
                Q(),
            )

            queryset = Place.objects.filter(place_query)

        return Response(PlaceSerializer(queryset, many=True).data)
