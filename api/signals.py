from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from event_management import settings
from .models import EventRegistration


@receiver(post_save, sender=EventRegistration)
def send_registration_notification(sender, instance, created, **kwargs):
    if created:
        event, user_email = instance.event, instance.user.email
        subject = f'You are registered for {event.title}'
        html_message = render_to_string('api/email_notification.html', {'event': event})
        plain_message = strip_tags(html_message)
        send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [user_email], html_message=html_message)
