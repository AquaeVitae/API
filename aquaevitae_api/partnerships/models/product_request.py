from django.db import models

from products.models.product import Product 
from partnerships.models.request import RequestBaseModel
from partnerships.models import Partnership

class ProductRequest(RequestBaseModel, Product):
    partnership = models.ForeignKey(Partnership, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="products")
