from hashlib import md5

from django.db import models
from django.utils.translation import gettext_lazy as _

from aquaevitae_api.storage import OverwriteStorage
from aquaevitae_api.models import BaseModel, OneToManyBaseModel
from products.models.base import ProductBase
from companies.models import Company
from products.constants import (
    ProductSkinTypeChoices,
    SKIN_NEEDS_CHOICES,
    SOLAR_CARES_CHOICES,
    DISEASE_NEEDS_MAP
)
from recommendations.constants import FormSkinDiseasesLevelChoices


def upload_to(instance, filename):
    return f"products/{md5(instance.id.hex.encode('utf-8')).hexdigest()}.{filename.split('.')[-1]}"


class Product(ProductBase, BaseModel):
    image = models.ImageField(
        upload_to=upload_to,
        storage=OverwriteStorage(),
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        Company,
        null=False,
        blank=False,
        on_delete=models.DO_NOTHING,
        related_name="products",
    )

    class Meta:
        db_table = "product"
        verbose_name = _("Product")

    def get_score(self, form):
        score = 0
        product_skin_needs = set([skin_need.skin_need for skin_need in self.skin_needs.all()])

        for disease in form.skin_diseases.all():
            if disease.level == FormSkinDiseasesLevelChoices.NONE:
                continue
            
            form_skin_needs = set(DISEASE_NEEDS_MAP[disease.skin_disease])

            related_skin_needs = product_skin_needs.intersection(form_skin_needs)

            score += len(related_skin_needs) * disease.level

        score += round(int(9 in product_skin_needs) * form.aging_level)

        form_skin_types = set([skin_type.skin_type for skin_type in form.skin_types.all()])
        product_skin_types = set([skin_type.skin_type for skin_type in self.skin_types.all()])
        related_skin_types = product_skin_types.intersection(form_skin_types)
        
        score += (len(related_skin_types) + 1) ** 2 if related_skin_needs else 0

        return score


class Ingredients(OneToManyBaseModel):
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


class SkinType(OneToManyBaseModel):
    product = models.ForeignKey(
        Product, related_name="skin_types", on_delete=models.CASCADE
    )
    skin_type = models.SmallIntegerField(blank=True, choices=ProductSkinTypeChoices.choices)

    class Meta:
        unique_together = (
            "product",
            "skin_type",
        )

    def __str__(self):
        return self.get_skin_type_display()


class SkinNeeds(OneToManyBaseModel):
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


class SkinSolarNeeds(OneToManyBaseModel):
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
