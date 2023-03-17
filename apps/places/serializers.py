from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Place


class AddressSerializer(serializers.Serializer):
    isolatedDwelling = serializers.CharField(allow_blank=True, allow_null=True)
    cityBlock = serializers.CharField(allow_blank=True, allow_null=True)
    houseNumber = serializers.CharField(allow_blank=True, allow_null=True)
    houseName = serializers.CharField(allow_blank=True, allow_null=True)
    manMade = serializers.CharField(allow_blank=True, allow_null=True)
    mountainPass = serializers.CharField(allow_blank=True, allow_null=True)
    stateDistrict = serializers.CharField(allow_blank=True, allow_null=True)
    countryCode = serializers.CharField(allow_blank=True, allow_null=True)
    cityDistrict = serializers.CharField(allow_blank=True, allow_null=True)
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


class PlaceSerializer(serializers.ModelSerializer):
    address = AddressField()

    class Meta:
        model = Place
        fields = '__all__'


class NominatimLookupQuerySerializer(serializers.Serializer):
    osm_type = serializers.ChoiceField(choices=('node', 'way', 'relation'))
    osm_id = serializers.IntegerField()
    category = serializers.CharField()


class NominatimSearchQuerySerializer(serializers.Serializer):
    viewbox = serializers.CharField()
    q = serializers.CharField()
