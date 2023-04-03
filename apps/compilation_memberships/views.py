from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .models import CompilationMembership
from .permissions import CanEditCompilationMembershipRole, CanDeleteCompilationMembership
from .serializers import CompilationMembershipCreateSerializer, CompilationMembershipSerializer


class CompilationMembershipsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['compilation', 'role']

    def get_queryset(self):
        query = Q(compilation__is_private=False)

        if self.request.user.is_authenticated:
            query |= Q(
                compilation__is_private=True,
                compilation__compilationmembership__user=self.request.user,
            )

        return CompilationMembership.objects.filter(query)

    def get_serializer_class(self):
        if self.action == 'create':
            return CompilationMembershipCreateSerializer

        return CompilationMembershipSerializer

    def get_permissions(self):
        if self.action == 'create':
            return (IsAuthenticated(),)

        if self.action in ('update', 'partial_update'):
            return (IsAuthenticated(), CanEditCompilationMembershipRole())

        if self.action in ('destroy'):
            return (IsAuthenticated(), CanDeleteCompilationMembership(),)

        return []

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
