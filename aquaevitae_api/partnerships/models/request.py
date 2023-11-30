from django.db import models

from partnerships.constants import REQUEST_STATUS_CHOICES

class RequestBaseModel(models.Model):
    approved_date = models.DateTimeField(null=True, blank=True)
    comments = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=1, choices=REQUEST_STATUS_CHOICES)

    class Meta:
        abstract = True

    @property
    def is_approved(self):
        return self.status == "A"
