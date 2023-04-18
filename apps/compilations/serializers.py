from rest_framework import serializers
from .models import Compilation
from apps.places.models import Place
from apps.users.serializers import UserSerializer, User


class CompilationSerializer(serializers.ModelSerializer):
    color_regex = r'^#[0-9a-f]{6}$'
    primary_color = serializers.RegexField(color_regex, required=False)
    secondary_color = serializers.RegexField(color_regex, required=False)
    owner = UserSerializer(read_only=True)
    description = serializers.CharField(required=False)

    class Meta:
        model = Compilation
        fields = ('id', 'primary_color', 'secondary_color', 'is_private', 'name', 'description', 'owner')


class CompilationPlacesSerializer(serializers.Serializer):
    place_ids = serializers.PrimaryKeyRelatedField(
        queryset=Place.objects.all(),
        many=True
    )
