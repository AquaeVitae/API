import asyncio

from django.contrib.auth.models import User, Group
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils import timezone

from aquaevitae_api.mail.utils import async_send_mail, async_send_mass_mail
from aquaevitae_api.mail.messages import REQUEST_STATUS_UPDATE_SUBJECT, REQUEST_STATUS_DENIED_MESSAGE, REQUEST_STATUS_APPROVED_MESSAGE, REQUEST_CREATED_ADMIN_SUBJECT, REQUEST_CREATED_ADMIN_MESSAGE, REQUEST_CREATED_MESSAGE, REQUEST_CREATED_SUBJECT, REQUEST_DENIED_BY_SERVER_MESSAGE
from partnerships.models import PartnershipRequest
from partnerships.constants import RequestStatusChoices


@receiver(post_save, sender=PartnershipRequest)
def notify_partnership_stakeholders(sender, instance, created, update_fields, *args, **kwargs):
    if not created:
        if instance.previous_status and instance.previous_status != instance.status:
            match instance.status:
                case RequestStatusChoices.DENIED:
                    asyncio.run(async_send_mail(
                        subject=REQUEST_STATUS_UPDATE_SUBJECT,
                        message=REQUEST_STATUS_DENIED_MESSAGE % instance.agent_fullname,
                        recipient_list=[instance.agent_email],
                        fail_silently=True,
                        from_email=None
                    ))
                case RequestStatusChoices.APPROVED:
                    asyncio.run(async_send_mail(
                        subject=REQUEST_STATUS_UPDATE_SUBJECT,
                        message=REQUEST_STATUS_APPROVED_MESSAGE % instance.agent_fullname,
                        recipient_list=[instance.agent_email],
                        fail_silently=True,
                        from_email=None
                    ))
    else:
        if instance.status == RequestStatusChoices.DENIED_BY_SERVER:
            asyncio.run(async_send_mail(
                        subject=REQUEST_CREATED_SUBJECT,
                        message= REQUEST_DENIED_BY_SERVER_MESSAGE % (instance.agent_fullname, instance.id),
                        recipient_list=[instance.agent_email],
                        fail_silently=True,
                        from_email=None
                    ))
        else:
            customer_email = (
                    REQUEST_CREATED_SUBJECT,
                    REQUEST_CREATED_MESSAGE % (instance.agent_fullname, instance.id),
                    None,
                    [instance.agent_email],
                )
            
            admin_addresses = set(User.objects.distinct("email").values_list("email", flat=True))
            admin_email = (
                    REQUEST_CREATED_ADMIN_SUBJECT % instance.company_name,
                    REQUEST_CREATED_ADMIN_MESSAGE % (instance.id, instance.company_name, instance.agent_fullname, instance.agent_role, instance.agent_email, instance.phone, instance.agent_message),
                    None,
                    admin_addresses,
                )

            messages = (customer_email,admin_email)
            asyncio.run(async_send_mass_mail(messages, fail_silently=True))
