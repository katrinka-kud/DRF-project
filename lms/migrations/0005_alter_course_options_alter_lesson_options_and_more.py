# Generated by Django 4.2 on 2024-06-16 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("lms", "0004_subscription"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="course",
            options={
                "ordering": ["pk"],
                "verbose_name": "курс",
                "verbose_name_plural": "курсы",
            },
        ),
        migrations.AlterModelOptions(
            name="lesson",
            options={
                "ordering": ["pk"],
                "verbose_name": "урок",
                "verbose_name_plural": "уроки",
            },
        ),
        migrations.AlterField(
            model_name="subscription",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to="lms.course",
                verbose_name="курс",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriptions",
                to=settings.AUTH_USER_MODEL,
                verbose_name="пользователь",
            ),
        ),
    ]
