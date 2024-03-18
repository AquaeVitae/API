from django.db import models

from aquaevitae_api.models import BaseModel, SetField

from partnerships.models.base import RequestBaseModel
from partnerships.models import Partnership
from products.models.base import ProductBase
from products.constants import (
    SKIN_TYPE_CHOICES,
)


class ProductRequest(RequestBaseModel, ProductBase, BaseModel):
    partnership = models.ForeignKey(
        Partnership,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="products",
    )

    skin_types = SetField(
        models.SmallIntegerField(blank=True, choices=SKIN_TYPE_CHOICES),
        size=len(SKIN_TYPE_CHOICES),
        default=list,
        null=False,
        blank=False,
    )

    ingredients = SetField(
        models.CharField(blank=False, null=False), default=list, null=False, blank=False
    )
