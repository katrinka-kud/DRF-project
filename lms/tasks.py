from datetime import datetime, timezone, timedelta

from celery import shared_task
from django.conf import settings

from lms.models import Course, Subscription
from users.models import User


@shared_task
def send_email(course_id):
    course = Course.objects.get(pk=course_id)
    search_subscribers = Subscription.objects.get(course=course_id)

    send_email(
        subject=f'Курс "{course}" обновлен',
        message=f'Обновился курс "{course}" на который вы подписаны',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[search_subscribers.user.email]
    )


@shared_task
def check_inactive_users():
    active_users = User.objects.filter(is_active=True)
    now = datetime.now(timezone.utc)
    for user in active_users:
        if user.last_login:
            if now - user.last_login > timedelta(days=30):
                user.is_active = False
                user.save()
                print(f"Пользователь {user} заблокирован")
