from django.db import models

from aquaevitae_api.models.base import BaseModel
from partnerships.models.base import RequestBaseModel
from phonenumber_field.modelfields import PhoneNumberField


class PartnershipRequest(RequestBaseModel, BaseModel):
    company_name = models.CharField(null=False, blank=False, max_length=100)
    agent_fullname = models.CharField(
        null=False, blank=False, max_length=30
    )
    agent_role = models.CharField(null=True, blank=False, max_length=30)
    agent_email = models.EmailField(
        null=False, blank=False, max_length=100
    )
    phone = PhoneNumberField(null=True, blank=False)
    country = models.CharField(null=False, blank=False, max_length=30)
    agent_message = models.TextField(null=False, blank=False, max_length=500)

    class Meta:
        db_table = "partnership_request"
