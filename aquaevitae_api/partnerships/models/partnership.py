from django.db import models

from aquaevitae_api.models import BaseModel
from companies.models import Company
from partnerships.models import CompanyRequest
from partnerships.constants import PARTNERSHIP_STATUS_CHOICES


class Partnership(BaseModel):
    status = models.CharField(max_length=1, choices=PARTNERSHIP_STATUS_CHOICES)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(
        Company, null=True, blank=True, on_delete=models.DO_NOTHING, related_name="+"
    )
    company_request = models.ForeignKey(
        CompanyRequest, null=True, blank=True, on_delete=models.DO_NOTHING
    )
    closed_date = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "partnership"
