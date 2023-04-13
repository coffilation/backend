from rest_framework import serializers


class PermissionSerializer(serializers.Serializer):
    permission = serializers.CharField()
