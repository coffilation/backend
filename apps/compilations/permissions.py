from rest_framework.permissions import BasePermission

from .models import CompilationPermission


class CanEditCompilation(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.has_perm(CompilationPermission.CHANGE_COMPILATION, request.user)


class CanChangeCompilationPlaces(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.has_perm(CompilationPermission.CHANGE_PLACES_LIST, request.user)


class CanDeleteCompilation(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
