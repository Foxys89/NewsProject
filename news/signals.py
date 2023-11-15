from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .models import Post


def send_notifications(preview, pk, title, subscribers):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{settings.SITE_URL}/news/{pk}',
        }
    )

    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()


@receiver(m2m_changed, sender=Post)
def new_post_notify(sender, instance, created, **kwargs):
    if created:
        subject = f'Новая публикация {Post.post_name} {Post.post_time}'
    else:
        subject = f'Публикация была изменена: {Post.post_name} {Post.post_time}'

    categories = instance.post_category.all()
    subscribers = []
    for category in categories:
        subscribers += category.subscribers.all()

    subscribers = [s.email for s in subscribers]

    send_notifications(instance.post_text, instance.pk, instance.post_name, subscribers)