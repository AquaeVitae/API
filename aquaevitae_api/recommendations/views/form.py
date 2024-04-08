import asyncio

from rest_framework import permissions, mixins
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from aquaevitae_api.mail.utils import async_send_mail
from aquaevitae_api.mail.messages import (
    RECOMMENDATIONS_MESSAGE,
    RECOMMENDATIONS_SUBJECT,
)
from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from recommendations.serializers import CreateFormSerializer, DetailFormSerializer
from recommendations.models import Form


class FormViewSet(
    mixins.CreateModelMixin,
    AtomicTransactionMixin,
    BaseViewSet,
):
    queryset = Form.objects.all().order_by("-created_at")
    permission_classes = [
        permissions.AllowAny,
    ]
    create_serializer_class = CreateFormSerializer
    retrieve_serializer_class = DetailFormSerializer

    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.user_email:
            asyncio.run(
                async_send_mail(
                    subject=RECOMMENDATIONS_SUBJECT,
                    message=RECOMMENDATIONS_MESSAGE
                    % (
                        instance.user_name,
                        f"{settings.FRONTEND_URL}/products?form_id={instance.id}",
                    ),
                    recipient_list=[instance.user_email],
                    fail_silently=True,
                    from_email=None,
                )
            )

        return instance
