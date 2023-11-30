from django.utils.translation import gettext_lazy as _

REQUEST_STATUS_CHOICES = [
    ("A", _("Approved")),
    ("W", _("Waiting")),
    ("D", _("Denied")),
]

PARTNERSHIP_STATUS_CHOICES = [
    ("O", _("Open")),
    ("C", _("Closed")),
]
