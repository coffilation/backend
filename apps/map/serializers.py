from rest_framework import serializers

from apps.map.constants import viewbox_pattern


class MapPlacesQuerySerializer(serializers.Serializer):
    compilation = serializers.ListField(child=serializers.IntegerField(), required=False)
    viewbox = serializers.RegexField(viewbox_pattern)
