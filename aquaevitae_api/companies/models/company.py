from django.db import models
from django.utils.translation import gettext_lazy as _

from aquaevitae_api.models import BaseModel
from companies.models.base import CompanyBaseModel


class Company(CompanyBaseModel, BaseModel):
    assigned_partnership = models.OneToOneField(
        "partnerships.PartnershipRequest",
        null=True,
        blank=True,
        on_delete=models.DO_NOTHING,
        related_name="created_company",
    )

    class Meta:
        db_table = "company"
        verbose_name_plural = _("Companies")
        verbose_name = _("Company")
