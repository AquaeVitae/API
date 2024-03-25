from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField
from django.utils.translation import gettext_lazy as _

from aquaevitae_api.models.base import BaseModel
from partnerships.models.base import RequestBaseModel
from phonenumber_field.modelfields import PhoneNumberField
from partnerships.constants import RequestStatusChoices

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
    country = CountryField()
    agent_message = models.TextField(null=False, blank=False, max_length=500)
    previous_status = None

    def __init__(self, *args, **kwargs) -> None:
        super(PartnershipRequest, self).__init__(*args, **kwargs)
        self.previous_status = self.status

    def save(self, *args, **kwargs) -> None:
        if self.previous_status and self.status != self.previous_status:
            if self.status == RequestStatusChoices.APPROVED:
                self.approved_date = timezone.now()            

        model = super(PartnershipRequest, self).save(*args, **kwargs)
        return model

    class Meta:
        db_table = "partnership_request"
        verbose_name = _("Partnership Request")
