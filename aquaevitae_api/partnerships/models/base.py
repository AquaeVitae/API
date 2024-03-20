from django.db import models

from partnerships.constants import RequestStatusChoices


class RequestBaseModel(models.Model):
    approved_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=RequestStatusChoices.choices, default=RequestStatusChoices.WAITING)

    class Meta:
        abstract = True

    @property
    def is_approved(self) -> bool:
        return self.status == "A"
