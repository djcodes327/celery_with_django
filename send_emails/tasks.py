from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
from celery_with_django import settings


@shared_task(bind=True)
def send_user_email(self):
    user = get_user_model().objects.get(username="djcodes")
    mail_subject = "Demo Subject"
    message = "Your Test Message"
    to_email = user.email
    send_mail(
        subject=mail_subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        fail_silently=True,
    )
    return "Done"
