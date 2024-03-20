from django.core.mail import send_mail, send_mass_mail

async def async_send_mail(*args, **kwargs):
    send_mail(*args, **kwargs)

async def async_send_mass_mail(*args, **kwargs):
    send_mass_mail(*args, **kwargs)
