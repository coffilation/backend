import django_filters
from django_filters import filters

from apps.places.models import Place


class MapPlaceFilterSet(django_filters.FilterSet):
    lat = filters.NumericRangeFilter(field_name='lat', lookup_expr='range', required=True)
    lon = filters.NumericRangeFilter(field_name='lon', lookup_expr='range', required=True)

    class Meta:
        model = Place
        fields = ['compilation']
