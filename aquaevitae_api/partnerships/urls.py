from django.urls import include, path
from rest_framework import routers


from partnerships.views import PartnershipViewSet

router = routers.DefaultRouter()
router.register(r'partnerships', PartnershipViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
