from rest_framework.permissions import BasePermission

from .models import CompilationPermission


class CanEditCompilation(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm(CompilationPermission.CHANGE_COMPILATION, obj)


class CanChangeCompilationPlaces(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm(CompilationPermission.CHANGE_PLACES_LIST, obj)


class CanDeleteCompilation(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
