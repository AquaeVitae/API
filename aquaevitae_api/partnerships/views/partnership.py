from rest_framework import permissions, viewsets

from partnerships.serializers import CreatePartnershipSerializer, DefaultPartnershipSerializer
from partnerships.models import Partnership

class PartnershipViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Partnership.objects.all().order_by('-created_at')
    serializer_class = DefaultPartnershipSerializer
    permission_classes = [permissions.AllowAny,]