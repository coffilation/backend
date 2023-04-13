from rest_framework.permissions import BasePermission

from apps.compilation_memberships.models import CompilationMembership
from apps.compilations.models import Compilation


class IsCollectionOwner(BasePermission):
    def has_permission(self, request, view):
        return view.kwargs['user_id'] != request.user.id and Compilation.objects.filter(
            id=view.kwargs['compilation_id'],
            owner=request.user,
        ).exists()


class IsCollectionStaff(BasePermission):
    def has_permission(self, request, view):
        return CompilationMembership.objects.filter(
            user=request.user,
            compilation_id=view.kwargs['compilation_id'],
            is_staff=True,
        ).exists()
