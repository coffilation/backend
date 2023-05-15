import re
import django_filters
from django.contrib.gis.geos import Polygon
from rest_framework import serializers

from apps.compilations.models import Compilation
from apps.map.constants import viewbox_pattern
from apps.places.models import Place


class MapPlacesFilterSet(django_filters.FilterSet):
    class Meta:
        model = Place
        fields = []

    compilation = django_filters.ModelMultipleChoiceFilter(
        required=True,
        queryset=Compilation.objects.all(),
    )
    viewbox = django_filters.CharFilter(field_name='geometry', method='filter_by_viewbox')

    def filter_by_viewbox(self, queryset, name, value):
        if not re.match(viewbox_pattern, value):
            raise serializers.ValidationError()

        return queryset.filter(**{ f'{name}__coveredby': Polygon.from_bbox(value.split(',')) })
