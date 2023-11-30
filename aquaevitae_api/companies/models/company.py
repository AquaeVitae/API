from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from aquaevitae_api.models import BaseModel


class Company(BaseModel):
    name = models.CharField(null=False, blank=False, unique=True, max_length=100)
    agent_fullname = models.CharField(null=False, blank=False, unique=False, max_length=30)
    agent_role = models.CharField(null=True, blank=False, unique=False, max_length=30)
    agent_email = models.EmailField(null=False, blank=False, unique=True, max_length=100)
    phone = PhoneNumberField(null=True, blank=False, unique=True)
    country = models.CharField(null=False, blank=False, unique=True, max_length=30)
    assigned_partnership = models.OneToOneField("partnerships.Partnership", null=True, blank=True, on_delete=models.DO_NOTHING, related_name='created_company')
