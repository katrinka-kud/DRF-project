from django.contrib.auth.models import AbstractUser
from django.db import models

from lms.models import NULLABLE, Course, Lesson


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True, verbose_name="почта", help_text="Укажите почту"
    )

    phone = models.CharField(
        max_length=35,
        verbose_name="номер телефона",
        help_text="Укажите телефон",
        **NULLABLE,
    )
    city = models.CharField(
        max_length=100, verbose_name="город", help_text="Укажите город", **NULLABLE
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        verbose_name="аватар",
        help_text="Загрузите аватар",
        **NULLABLE,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"

    def __str__(self):
        return self.email


class Payments(models.Model):
    PAYMENT_CARD = "оплата картой"
    PAYMENT_CASH = "оплата наличными"

    PAYMENT_CHOICES = (
        (PAYMENT_CARD, "оплата картой"),
        (PAYMENT_CASH, "оплата наличными"),
    )

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="пользователь"
    )
    date_payment = models.DateField(
        auto_now=True, verbose_name="дата оплаты", help_text="Укажите дату оплаты"
    )
    paid_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, verbose_name="оплаченный курс", **NULLABLE
    )
    paid_lesson = models.ForeignKey(
        Lesson, on_delete=models.CASCADE, verbose_name="оплаченный урок", **NULLABLE
    )
    sum_payment = models.DecimalField(
        max_digits=15, decimal_places=2, verbose_name="сумма оплаты"
    )
    payment_method = models.CharField(
        max_length=20,
        default=PAYMENT_CARD,
        choices=PAYMENT_CHOICES,
        verbose_name="способ оплаты"
    )

    session_id = models.CharField(
        max_length=255,
        **NULLABLE,
        verbose_name="идентификатор сессии"
    )
    link = models.URLField(
        max_length=400,
        **NULLABLE,
        verbose_name="ссылка на оплату"
    )
    session_status = models.CharField(
        max_length=50,
        **NULLABLE,
        verbose_name="статус оплаты"
    )

    is_paid = models.BooleanField(default=False, verbose_name="оплачено")

    class Meta:
        verbose_name = "платеж"
        verbose_name_plural = "платежи"

    def __str__(self):
        return f"""{self.paid_course if self.paid_course else self.paid_lesson}\n
                   \rСумма платежа: {self.sum_payment}\n
                   \rСпособ оплаты: {self.payment_method}\n
                """
