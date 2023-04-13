from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from apps.compilation_permissions import views

base_path = 'compilation_permissions'

compilation_permissions_urls = [
    path('', views.CompilationPermissionsList.as_view()),
    path(
        '<int:compilation_id>/<int:user_id>/',
        views.CompilationPermissionsUserPermissions.as_view()
    ),
    path(
            '<int:compilation_id>/<int:user_id>/<str:permission>',
        views.CompilationPermissionsChangeUserPermissions.as_view()
    ),
]
