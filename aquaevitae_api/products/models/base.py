from django.db import models

from products.constants import (
    CATEGORY_CHOICES,
    SIZE_TYPE_CHOICES,
    SKIN_TYPE_CHOICES,
    PRODUCT_TYPE_CHOICES,
)


class ProductBase(models.Model):
    name = models.CharField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    size = models.FloatField()
    size_type = models.CharField(max_length=2, choices=SIZE_TYPE_CHOICES)
    characteristics = models.TextField()
    recommended_use = models.TextField()
    contraindications = models.TextField()

    class Meta:
        abstract = True
