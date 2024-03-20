import asyncio

from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _

from rest_framework import permissions, mixins, exceptions
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT

from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from partnerships.serializers import CreatePartnershipSerializer
from partnerships.models import PartnershipRequest


async def async_send_mail(model, target, exception = False):
    if exception:
        send_mail(
            subject=_('Partnership Request Received of company ') + model.company_name,
            message=str(model.id),
            recipient_list=[target],
            fail_silently=True,
            from_email=None
        )
    else:
        send_mail(
            subject=_('Partnership Request Received of company ') + model.company_name,
            message=str(model.id),
            recipient_list=[target],
            fail_silently=True,
            from_email=None
        )

class PartnershipViewSet(mixins.CreateModelMixin, AtomicTransactionMixin, BaseViewSet):
    queryset = PartnershipRequest.objects.all().order_by('-created_at')
    serializer_class = CreatePartnershipSerializer
    permission_classes = [permissions.AllowAny,]

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(status=HTTP_204_NO_CONTENT)
