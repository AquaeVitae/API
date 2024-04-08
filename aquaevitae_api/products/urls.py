from django.urls import include, path
from rest_framework import routers


from products.views import ProductsViewSet

router = routers.DefaultRouter()
router.register(r"products", ProductsViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]
