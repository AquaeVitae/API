from celery import chord, group
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions, mixins
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED
from rest_framework.parsers import MultiPartParser

from aquaevitae_api.views import BaseViewSet
from analysis.serializers import CreateFacialAnalysisSerializer, ResponseFacialAnalysisSerializer, DetailsFacialAnalysisSerializer
from analysis.models import FacialAnalysis
from analysis.tasks import process_wrinkles_facial_analysis, set_as_done


class FacialAnalysisViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, BaseViewSet):
    queryset = FacialAnalysis.objects.all().order_by("-created_at").prefetch_related("predictions")
    serializer_class = ResponseFacialAnalysisSerializer
    create_serializer_class = CreateFacialAnalysisSerializer
    parser_classes = [MultiPartParser,]
    permission_classes = [
        permissions.AllowAny,
    ]
    retrieve_serializer_class = DetailsFacialAnalysisSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        tasks = (process_wrinkles_facial_analysis.s(analysis_id=instance.id),)
        callback = set_as_done.s(analysis_id=instance.id)
        chord(tasks)(callback)

    def create(self, request, *args, **kwargs):
        serializer = super().create(request, *args, **kwargs)
        return Response(ResponseFacialAnalysisSerializer().to_representation(serializer.data), status=HTTP_201_CREATED)