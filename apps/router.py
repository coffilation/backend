from rest_framework import routers
from django.urls import path, include

from apps.compilation_permissions.urls import compilation_permissions_urls
from apps.map.views import MapPlacesViewSet
from apps.places.views import PlaceViewSet, NominatimPlaceViewSet
from apps.compilations.views import CompilationPopulatedByPlaceViewSet, CompilationViewSet
from apps.compilation_memberships.views import CompilationMembershipsViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet, 'places')
router.register(r'nominatim', NominatimPlaceViewSet, 'nominatim')
router.register(
    r'compilations/populated_by_place',
    CompilationPopulatedByPlaceViewSet,
    'compilations_populated_by_place'
)
router.register(r'compilations', CompilationViewSet, 'compilation')
router.register(
    r'compilation_memberships',
    CompilationMembershipsViewSet,
    'compilation_memberships'
)
router.register(r'map/places', MapPlacesViewSet, 'map_places')

urlpatterns = [
    path('', include(router.urls)),
    path('compilation_permissions/', include(compilation_permissions_urls)),
]
