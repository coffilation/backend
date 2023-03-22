from rest_framework.permissions import BasePermission

from apps.compilation_memberships.models import CompilationMembership, CompilationMembershipRole


class CanEditCompilation(BasePermission):
    def has_object_permission(self, request, view, obj):
        user_role = CompilationMembership.objects.get(user=request.user, compilation=obj).role

        return user_role >= CompilationMembershipRole.EDITOR


class CanDeleteCompilation(BasePermission):
    def has_object_permission(self, request, view, obj):
        user_role = CompilationMembership.objects.get(user=request.user, compilation=obj).role

        return user_role >= CompilationMembershipRole.OWNER
