from celery import shared_task
from django.core.mail import send_mail
from django.utils.timezone import now
from datetime import timedelta
from .models import User

@shared_task
def send_welcome_email(user_email):
    subject = "Добро пожаловать в Sales Trading!"
    message = "Спасибо за регистрацию в нашем сервисе. Удачной торговли!"
    send_mail(subject, message, 'noreply@salestrading.com', [user_email])
    return f"Email отправлен на {user_email}"

@shared_task
def delete_inactive_users():
    one_week_ago = now() - timedelta(days=7)
    inactive_users = User.objects.filter(is_active=False, date_joined__lt=one_week_ago)
    count = inactive_users.count()
    inactive_users.delete()
    return f"Удалено {count} неактивных пользователей"
