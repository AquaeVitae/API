from rest_framework import viewsets
from django.db import transaction


class BaseViewSet(viewsets.GenericViewSet):
    def get_serializer_class(self):
        serializer = getattr(self, self.action + "_serializer_class", None)
        if not serializer:
            serializer = getattr(self, "serializer_class")
        return serializer
    
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class AtomicTransactionMixin:
    @classmethod
    def as_view(cls, actions=None, **initkwargs):
        view = super().as_view(actions, **initkwargs)
        return transaction.atomic()(view)
    