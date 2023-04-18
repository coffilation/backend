from rest_framework.permissions import BasePermission


class CanEditCompilationMembership(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.compilation__owner == request.user


class CanDeleteCompilationMembership(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.compilation__owner == request.user != obj.user
