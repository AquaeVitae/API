from enum import unique

from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


@unique
class RequestStatusChoices(TextChoices):
    APPROVED = "A", _("Approved")
    WAITING = "W", _("Waiting")
    DENIED = "D", _("Denied")
    DENIED_BY_SERVER = "S", _("Denied by Server")
