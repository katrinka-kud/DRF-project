from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name='почта',
        help_text='Укажите почту'
    )

    phone = models.CharField(
        max_length=35,
        verbose_name='номер телефона',
        help_text='Укажите телефон',
        **NULLABLE,
    )
    city = models.CharField(
        max_length=100,
        verbose_name='город',
        help_text='Укажите город',
        **NULLABLE
    )
    avatar = models.ImageField(
        upload_to='users/avatars',
        verbose_name='аватар',
        help_text='Загрузите аватар',
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
