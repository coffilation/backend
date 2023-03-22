from rest_framework import serializers
from .models import CompilationMembership, CompilationMembershipRole
from apps.users.serializers import UserSerializer
from ..compilations.models import Compilation


class CompilationMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CompilationMembership
        fields = ('id', 'user', 'role')


class CompilationMembershipCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    compilation = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Compilation.objects.all(),
    )

    class Meta:
        model = CompilationMembership
        fields = ('id', 'user', 'role', 'compilation')
        read_only_fields = ('role',)
