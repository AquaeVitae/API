from django.db import models

from aquaevitae_api.models import BaseModel
from products.models.base import ProductBase
from partnerships.models.partnership import Partnership
from products.constants import (
    SKIN_TYPE_CHOICES,
    PRODUCT_TYPE_CHOICES,
)


class Product(ProductBase, BaseModel):
    assigned_partnership = models.ForeignKey(
        Partnership,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="+",
    )

    class Meta:
        db_table = "product"


class Ingredients(models.Model):
    product = models.ForeignKey(
        Product, related_name="ingredients", on_delete=models.CASCADE
    )
    name = models.CharField()

    class Meta:
        unique_together = (
            "product",
            "name",
        )


class SkinType(models.Model):
    product = models.ForeignKey(
        Product, related_name="skin_types", on_delete=models.CASCADE
    )
    skin_type = models.SmallIntegerField(blank=True, choices=SKIN_TYPE_CHOICES)

    class Meta:
        unique_together = (
            "product",
            "skin_type",
        )


class Type(models.Model):
    product = models.ForeignKey(Product, related_name="types", on_delete=models.CASCADE)
    product_type = models.SmallIntegerField(blank=False, choices=PRODUCT_TYPE_CHOICES)

    class Meta:
        unique_together = (
            "product",
            "product_type",
        )
