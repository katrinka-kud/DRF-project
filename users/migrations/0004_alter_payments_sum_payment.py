# Generated by Django 4.2 on 2024-06-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_payments_is_paid_payments_link_payments_session_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payments",
            name="sum_payment",
            field=models.PositiveIntegerField(verbose_name="сумма оплаты"),
        ),
    ]