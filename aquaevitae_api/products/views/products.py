from rest_framework import permissions, mixins

from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from products.serializers import DetailProductSerializer
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
    filterset_fields = {
            "category": ["in", "exact"],
            "type": ["in", "exact"],
            "skin_types__skin_type": ["in", "exact"],
            "skin_needs__skin_need": ["in", "exact"],
        }
    serializer_class = DetailProductSerializer
    search_fields = ['name', 'ingredients__name']
    ordering_fields = ["created_at", "price"]

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        if request.query_params.get("form_id"):
            response.data = sorted(response.data, key=lambda k: (k['score'], ), reverse=True)
        return response
