from django.db import models

from aquaevitae_api.models import BaseModel, SetField
from partnerships.models.partnership import Partnership
from products.constants import CATEGORY_CHOICES, SIZE_TYPE_CHOICES, SKIN_TYPE_CHOICES, PRODUCT_TYPE_CHOICES

class Product(BaseModel):
    name = models.CharField()
    assigned_partnership = models.ForeignKey(Partnership, null=True, blank=True, on_delete=models.DO_NOTHING)
    
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    size = models.FloatField()
    size_type = models.CharField(max_length=2, choices=SIZE_TYPE_CHOICES)

    characteristics = models.TextField()
    recommended_use = models.TextField()
    contraindications = models.TextField()


class ProductIngredients(models.Model):
    product_id = models.ForeignKey(Product, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField()

class ProductSkinType(models.Model):
    product_id = models.ForeignKey(Product, related_name="skin_types", on_delete=models.CASCADE)
    skin_type = models.SmallIntegerField(blank=True, choices=SKIN_TYPE_CHOICES)
    
    class Meta:
        unique_together = ('product_id', 'skin_type',)

class ProductType(models.Model):
    product_id = models.ForeignKey(Product, related_name="types", on_delete=models.CASCADE)
    product_type = models.SmallIntegerField(blank=False, choices=PRODUCT_TYPE_CHOICES)
    
    class Meta:
        unique_together = ('product_id', 'product_type',)
