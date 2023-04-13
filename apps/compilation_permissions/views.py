from django.contrib.auth.models import User
from django.http import Http404
from drf_spectacular.utils import OpenApiResponse, extend_schema
from guardian.shortcuts import assign_perm, get_perms, remove_perm
from rest_framework import status, views
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.compilation_permissions.enums import CompilationPermission
from apps.compilation_permissions.permissions import IsCollectionOwner, IsCollectionStaff
from apps.compilations.models import Compilation


@extend_schema(
    responses=OpenApiResponse(
        response={
            'type': 'array',
            'items': { 'type': 'string' },
        }
    )
)
class CompilationPermissionsList(views.APIView):

    def get(self, request):
        return Response(CompilationPermission)


class CompilationPermissionsUserPermissions(views.APIView):
    permission_classes = [IsAuthenticated, IsCollectionStaff]

    @extend_schema(
        responses=OpenApiResponse(
            response={
                'type': 'array',
                'items': { 'type': 'string' },
            }
        )
    )
    def get(self, request, compilation_id, user_id):
        return Response(
            get_perms(
                get_object_or_404(User, pk=user_id),
                get_object_or_404(Compilation, pk=compilation_id),
            )
        )


class CompilationPermissionsChangeUserPermissions(views.APIView):
    permission_classes = [IsAuthenticated, IsCollectionOwner]

    @extend_schema(responses={ 204: None })
    def post(self, request, compilation_id, user_id, permission):
        if permission not in CompilationPermission:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        assign_perm(
            permission,
            get_object_or_404(User, pk=user_id),
            get_object_or_404(Compilation, pk=compilation_id),
        )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema(responses={ 204: None })
    def delete(self, request, compilation_id, user_id, permission):
        if permission not in CompilationPermission:
            raise Http404

        remove_perm(
            permission,
            get_object_or_404(User, pk=user_id),
            get_object_or_404(Compilation, pk=compilation_id),
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
