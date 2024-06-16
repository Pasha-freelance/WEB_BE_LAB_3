from datetime import datetime, time

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from lab1BE import settings

User = get_user_model()


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Todo App'
        message = f'Hi {instance.username}, thank you for registering at our site.'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [instance.email]
        send_mail(subject, message, email_from, recipient_list)

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'admin_notifications', {
                'type': 'send_notification',
                'message': f'New user registered: {instance.username}',
                'timestamp': datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
                'email': instance.email
            }
        )
