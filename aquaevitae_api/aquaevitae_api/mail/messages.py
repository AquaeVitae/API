from django.utils.translation import gettext_lazy as _


REQUEST_STATUS_UPDATE_SUBJECT = _(
    "Status Update of your Aquaevitae partnership request!"
)
REQUEST_STATUS_DENIED_MESSAGE = _(
    "Dear %s,\n\nThank you for interest to become one of our partners.\nUnfortunatelly, we were not able to proceed with our partnership in this moment.\nMaybe we can meet again in the future.\n\nKind Regards,\nAquaevitae Team."
)
REQUEST_STATUS_APPROVED_MESSAGE = _(
    "Dear %s,\n\nThank you for interest to become one of our partners.\nWe are happy to annouce that your request was approved and your products will be add to our platform soon.\n\nKind Regards,\nAquaevitae Team."
)
REQUEST_CREATED_SUBJECT = _("Your Aquaevitae's partnership request was received!")
REQUEST_CREATED_MESSAGE = _(
    "Dear %s,\n\nThank you for interest to become one of our partners.\nYour request was received and one of our employees will get in touch soon.\nNumber of your protocol: %s\n\nKind Regards,\nAquaevitae Team."
)
REQUEST_DENIED_BY_SERVER_MESSAGE = _(
    "Dear %s,\n\nThank you for interest to become one of our partners.\nUnfortunatelly, you're not able to become one of our partners in the moment.\nGet in touch with one of our employees for more informations.\nNumber of your protocol: %s\n\nKind Regards,\nAquaevitae Team."
)
REQUEST_CREATED_ADMIN_SUBJECT = _("A partnership request was received from %s!")
REQUEST_CREATED_ADMIN_MESSAGE = _(
    "Request ID: %s\nCompany Name: %s\nAgent Name: %s\nAgent Role: %s\nAgent Email: %s\nPhone Number: %s\nRequest Message: \n%s\n"
)

RECOMMENDATIONS_SUBJECT = _("Here is your Aquaevitae personalized skin care plan!")
RECOMMENDATIONS_MESSAGE = _(
    "Dear %s,\n\nHere is your customized skin care plan with the best thermal water products:\n%s\n\nKind Regards,\nAquaevitae Team."
)
