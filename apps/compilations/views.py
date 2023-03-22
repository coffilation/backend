from drf_spectacular.utils import extend_schema
from .serializers import Compilation, CompilationPlacesSerializer, CompilationSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated


class CompilationViewSet(viewsets.ModelViewSet):
    queryset = Compilation.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return []

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

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
