from django.db.models import Q
from drf_spectacular.utils import extend_schema
from guardian.shortcuts import assign_perm
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from apps.compilation_memberships.models import CompilationMembership
from apps.compilation_permissions.enums import CompilationPermission

from .serializers import Compilation, CompilationPlacesSerializer, CompilationSerializer
from .permissions import CanEditCompilation, CanDeleteCompilation, CanChangeCompilationPlaces


class CompilationViewSet(viewsets.ModelViewSet):
    filterset_fields = ['is_private', 'owner', 'places']

    def get_queryset(self):
        query = Q(is_private=False)

        if self.request.user.is_authenticated:
            query |= Q(compilationmembership__user=self.request.user)

        return Compilation.objects.filter(query).distinct()

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'add_places', 'remove_places'):
            return (IsAuthenticated(), CanEditCompilation())

        if self.action == 'destroy':
            return (IsAuthenticated(), CanDeleteCompilation())

        if self.action in ('add_places', 'remove_places'):
            return (IsAuthenticated(), CanChangeCompilationPlaces())

        return []

    def perform_create(self, serializer):
        owner = self.request.user
        compilation = serializer.save(owner=owner)

        for permission in CompilationPermission.choices:
            assign_perm(permission[0], owner, compilation)

        CompilationMembership.objects.create(
            compilation_id=serializer.data['id'],
            user=self.request.user,
            is_staff=True,
        )

    def get_serializer_class(self):
        if self.action in ('add_places', 'remove_places'):
            return CompilationPlacesSerializer
        return CompilationSerializer

    @extend_schema(responses={ 204: None })
    @action(detail=True, methods=['post'])
    def add_places(self, request, pk):
        compilation = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        compilation.places.add(*serializer.data['place_ids'])
        return Response(status=204)

    @extend_schema(responses={ 204: None })
    @action(detail=True, methods=['post'])
    def remove_places(self, request, pk):
        compilation = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        compilation.places.remove(*serializer.data['place_ids'])
        return Response(status=204)
