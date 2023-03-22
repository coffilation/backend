from rest_framework.permissions import BasePermission

from apps.compilation_memberships.models import CompilationMembershipRole


class CanEditCompilationMembershipRole(BasePermission):
    def has_object_permission(self, request, view, obj):
        user_role = view.get_queryset().get(user=request.user, compilation=obj.compilation).role

        return user_role >= CompilationMembershipRole.ADMIN \
            and user_role > obj.role \
            and user_role > request.data['role']


class CanDeleteCompilationMembership(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True

        user_role = view.get_queryset().get(user=request.user, compilation=obj.compilation).role

        return user_role >= CompilationMembershipRole.ADMIN and user_role > obj.role
