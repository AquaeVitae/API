from django.db import models

from aquaevitae_api.models import BaseModel
from companies.models.base import CompanyBaseModel


class Company(CompanyBaseModel, BaseModel):
    assigned_partnership = models.OneToOneField(
        "partnerships.Partnership",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="created_company",
    )

    class Meta:
        db_table = "company"
