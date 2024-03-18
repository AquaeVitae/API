from hashlib import md5

from django.db import models

from aquaevitae_api.storage import OverwriteStorage
from aquaevitae_api.models import BaseModel
from products.models.base import ProductBase
from partnerships.models.partnership import Partnership
from products.constants import (
    SKIN_TYPE_CHOICES,
    SKIN_NEEDS_CHOICES,
    SOLAR_CARES_CHOICES
)

def upload_to(instance, filename):
    return f"products/{md5(instance.id.hex.encode('utf-8')).hexdigest()}.{filename.split('.')[-1]}"

class Product(ProductBase, BaseModel):
    assigned_partnership = models.ForeignKey(
        Partnership,
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="+",
    )
    image = models.ImageField(upload_to=upload_to, storage=OverwriteStorage(), null=True, blank=True, )

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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.get_skin_type_display()


class SkinNeeds(models.Model):
    product = models.ForeignKey(
        Product, related_name="skin_needs", on_delete=models.CASCADE
    )
    skin_need = models.SmallIntegerField(blank=True, choices=SKIN_NEEDS_CHOICES)

    class Meta:
        unique_together = (
            "product",
            "skin_need",
        )

    def __str__(self):
        return self.get_skin_need_display()


class SkinSolarNeeds(models.Model):
    product = models.ForeignKey(
        Product, related_name="skin_solar_needs", on_delete=models.CASCADE
    )
    skin_solar_need = models.SmallIntegerField(blank=True, choices=SOLAR_CARES_CHOICES)

    class Meta:
        unique_together = (
            "product",
            "skin_solar_need",
        )

    def __str__(self):
        return self.get_skin_solar_need_display()
