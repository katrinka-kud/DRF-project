from django.contrib import admin

from users.models import Payments, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
    )


@admin.register(Payments)
class PaymentsAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "date_payment",
        "paid_course",
        "paid_lesson",
        "sum_payment",
        "payment_method",
    )
