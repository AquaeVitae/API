from django.urls import include, path
from rest_framework import routers


from recommendations.views import FormViewSet

router = routers.DefaultRouter()
router.register(r"forms", FormViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
