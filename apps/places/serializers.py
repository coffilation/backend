from django.contrib.gis.geos import GEOSGeometry, Point
from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Place


class AddressSerializer(serializers.Serializer):
    isolated_dwelling = serializers.CharField(allow_blank=True, allow_null=True)
    city_block = serializers.CharField(allow_blank=True, allow_null=True)
    house_number = serializers.CharField(allow_blank=True, allow_null=True)
    house_name = serializers.CharField(allow_blank=True, allow_null=True)
    man_made = serializers.CharField(allow_blank=True, allow_null=True)
    mountain_pass = serializers.CharField(allow_blank=True, allow_null=True)
    state_district = serializers.CharField(allow_blank=True, allow_null=True)
    country_code = serializers.CharField(allow_blank=True, allow_null=True)
    city_district = serializers.CharField(allow_blank=True, allow_null=True)
    amenity = serializers.CharField(allow_blank=True, allow_null=True)
    road = serializers.CharField(allow_blank=True, allow_null=True)
    district = serializers.CharField(allow_blank=True, allow_null=True)
    borough = serializers.CharField(allow_blank=True, allow_null=True)
    suburb = serializers.CharField(allow_blank=True, allow_null=True)
    subdivision = serializers.CharField(allow_blank=True, allow_null=True)
    hamlet = serializers.CharField(allow_blank=True, allow_null=True)
    croft = serializers.CharField(allow_blank=True, allow_null=True)
    neighbourhood = serializers.CharField(allow_blank=True, allow_null=True)
    allotments = serializers.CharField(allow_blank=True, allow_null=True)
    quarter = serializers.CharField(allow_blank=True, allow_null=True)
    residential = serializers.CharField(allow_blank=True, allow_null=True)
    farm = serializers.CharField(allow_blank=True, allow_null=True)
    farmyard = serializers.CharField(allow_blank=True, allow_null=True)
    industrial = serializers.CharField(allow_blank=True, allow_null=True)
    commercial = serializers.CharField(allow_blank=True, allow_null=True)
    retail = serializers.CharField(allow_blank=True, allow_null=True)
    emergency = serializers.CharField(allow_blank=True, allow_null=True)
    historic = serializers.CharField(allow_blank=True, allow_null=True)
    military = serializers.CharField(allow_blank=True, allow_null=True)
    natural = serializers.CharField(allow_blank=True, allow_null=True)
    landuse = serializers.CharField(allow_blank=True, allow_null=True)
    place = serializers.CharField(allow_blank=True, allow_null=True)
    railway = serializers.CharField(allow_blank=True, allow_null=True)
    aerialway = serializers.CharField(allow_blank=True, allow_null=True)
    boundary = serializers.CharField(allow_blank=True, allow_null=True)
    aeroway = serializers.CharField(allow_blank=True, allow_null=True)
    club = serializers.CharField(allow_blank=True, allow_null=True)
    craft = serializers.CharField(allow_blank=True, allow_null=True)
    leisure = serializers.CharField(allow_blank=True, allow_null=True)
    office = serializers.CharField(allow_blank=True, allow_null=True)
    shop = serializers.CharField(allow_blank=True, allow_null=True)
    tourism = serializers.CharField(allow_blank=True, allow_null=True)
    bridge = serializers.CharField(allow_blank=True, allow_null=True)
    tunnel = serializers.CharField(allow_blank=True, allow_null=True)
    waterway = serializers.CharField(allow_blank=True, allow_null=True)
    city = serializers.CharField(allow_blank=True, allow_null=True)
    town = serializers.CharField(allow_blank=True, allow_null=True)
    state = serializers.CharField(allow_blank=True, allow_null=True)
    village = serializers.CharField(allow_blank=True, allow_null=True)
    region = serializers.CharField(allow_blank=True, allow_null=True)
    postcode = serializers.CharField(allow_blank=True, allow_null=True)
    country = serializers.CharField(allow_blank=True, allow_null=True)
    municipality = serializers.CharField(allow_blank=True, allow_null=True)


@extend_schema_field(AddressSerializer)
class AddressField(serializers.JSONField):
    pass


class GeometryField(serializers.Field):
    def to_internal_value(self, data):
        return data

    def to_representation(self, value):
        return value


class PlaceSerializer(serializers.ModelSerializer):
    address = AddressField()
    geometry = GeometryField()

    class Meta:
        model = Place
        fields = (
            'id',
            'address',
            'osm_id',
            'osm_type',
            'display_name',
            'category',
            'type',
            'geometry',
        )

    def to_internal_value(self, data):
        data['geometry'] = Point(float(data['lon']), float(data['lat']))
        data = super().to_internal_value(data)
        return data

    def to_representation(self, instance):
        instance = super().to_representation(instance)

        geometry = instance['geometry']
        del instance['geometry']
        instance['lon'] = geometry.x
        instance['lat'] = geometry.y

        return instance


class NominatimLookupQuerySerializer(serializers.Serializer):
    osm_type = serializers.ChoiceField(choices=('node', 'way', 'relation'))
    osm_id = serializers.IntegerField()
    category = serializers.CharField()


class NominatimSearchQuerySerializer(serializers.Serializer):
    viewbox = serializers.CharField()
    q = serializers.CharField()
