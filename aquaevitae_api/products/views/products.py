from rest_framework import permissions, mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from products.serializers import DetailProductSerializer, CreateImageSerializer
from products.models import Product


class ProductsViewSet(mixins.ListModelMixin, AtomicTransactionMixin, BaseViewSet):
    queryset = (
        Product.objects.all()
        .order_by("-created_at")
        .prefetch_related("ingredients", "skin_types", "skin_needs")
    )
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = DetailProductSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.query_params.get("form_id"):
            response.data = sorted(response.data, key=lambda k: (k['score'], ), reverse=True)
        return response
