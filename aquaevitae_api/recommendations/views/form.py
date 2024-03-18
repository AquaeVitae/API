from rest_framework import permissions, viewsets, mixins
from django.template.loader import render_to_string

from aquaevitae_api.views import BaseViewSet, AtomicTransactionMixin
from recommendations.serializers import CreateFormSerializer, DetailFormSerializer
from recommendations.models import Form

class FormViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, AtomicTransactionMixin, BaseViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Form.objects.all().order_by('-created_at')
    permission_classes = [permissions.AllowAny,]
    create_serializer_class = CreateFormSerializer
    retrieve_serializer_class = DetailFormSerializer

    def perform_create(self, serializer):
        response = serializer.save()

        if response.user_email:
            pass

        return response

