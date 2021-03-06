from rest_framework import routers

from .viewsets.organization import OrganizationViewSet
from .viewsets.user import UserViewSet
from .viewsets.vehicle import VehicleViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'organizations', OrganizationViewSet)
router.register(r'users', UserViewSet)
router.register(r'vehicles', VehicleViewSet)

urlpatterns = router.urls
