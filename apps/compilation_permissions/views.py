from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from guardian.shortcuts import assign_perm, get_perms, remove_perm
from rest_framework import status, viewsets, mixins, generics, views
from rest_framework.response import Response

from apps.compilation_permissions.enums import CompilationPermission
from apps.compilations.models import Compilation


def get_user(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        raise Http404

    return user


def get_compilation(compilation_id):
    try:
        compilation = Compilation.objects.get(id=compilation_id)
    except Compilation.DoesNotExist:
        raise Http404

    return compilation


class CompilationPermissionsList(views.APIView):

    def get(self, request):
        return Response(CompilationPermission)


class CompilationPermissionsUserPermissions(views.APIView):

    def get(self, request, compilation_id, user_id):
        return Response(get_perms(get_user(user_id), get_compilation(compilation_id)))


class CompilationPermissionsChangeUserPermissions(views.APIView):
    def post(self, request, compilation_id, user_id, permission):
        if permission not in CompilationPermission:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        assign_perm(permission, get_user(user_id), get_compilation(compilation_id))

        return Response(status=status.HTTP_204_NO_CONTENT)

    def delete(self, request, compilation_id, user_id, permission):
        if permission not in CompilationPermission:
            raise Http404

        remove_perm(permission, get_user(user_id), get_compilation(compilation_id))

        return Response(status=status.HTTP_204_NO_CONTENT)


