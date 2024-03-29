from django.utils.translation import gettext_lazy as _

from rest_framework import permissions, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from partnerships.serializers import CreatePartnershipSerializer
from partnerships.models import PartnershipRequest


class PartnershipViewSet(mixins.CreateModelMixin, AtomicTransactionMixin, BaseViewSet):
    queryset = PartnershipRequest.objects.all().order_by("-created_at")
    serializer_class = CreatePartnershipSerializer
    permission_classes = [
        permissions.AllowAny,
    ]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=HTTP_204_NO_CONTENT)
