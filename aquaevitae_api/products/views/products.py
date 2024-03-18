from rest_framework import permissions, mixins
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from products.serializers import DetailProductSerializer, CreateImageSerializer
from products.models import Product

class ProductsViewSet(mixins.ListModelMixin, AtomicTransactionMixin, BaseViewSet):
    queryset = Product.objects.all().order_by('-created_at').prefetch_related("ingredients", "skin_types", "skin_needs")
    permission_classes = [permissions.AllowAny,]
    serializer_class = DetailProductSerializer

    @action(
        detail=True,
        methods=['post'],
        url_path="images",
        parser_classes=[MultiPartParser,],
        serializer_class=CreateImageSerializer
    )
    def post_image(self, request: Request, pk=None):
        product = self.get_object()

        product.image = request.data["image"]
        product.save()

        return Response(DetailProductSerializer(product).data)

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)