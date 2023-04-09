from rest_framework import routers
from django.urls import path, include

from apps.compilation_permissions.urls import compilation_permissions_urls
from apps.places.views import PlaceViewSet, NominatimPlaceViewSet
from apps.compilations.views import CompilationViewSet
from apps.compilation_memberships.views import CompilationMembershipsViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, 'places')
router.register(r'nominatim', NominatimPlaceViewSet, 'nominatim')
router.register(r'compilations', CompilationViewSet, 'compilation')
router.register(
    r'compilation_memberships',
    CompilationMembershipsViewSet,
    'compilation_memberships'
)

urlpatterns = [
    path('', include(router.urls)),
    path('compilation_permissions/', include(compilation_permissions_urls)),
]
