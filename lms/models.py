from django.conf import settings
from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="название", help_text="Укажите название курса"
    )
    description = models.TextField(
        verbose_name="описание", **NULLABLE, help_text="Укажите описание курса"
    )
    picture = models.ImageField(
        upload_to="lms/pictures",
        **NULLABLE,
        verbose_name="превью (картинка)",
        help_text="Загрузите картинку"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, **NULLABLE,
        verbose_name="владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"
        ordering = ("title",)


class Lesson(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="название", help_text="Укажите название урока"
    )
    description = models.TextField(
        verbose_name="описание", **NULLABLE, help_text="Укажите описание урока"
    )
    picture = models.ImageField(
        upload_to="lms/pictures",
        **NULLABLE,
        verbose_name="превью (картинка)",
        help_text="Загрузите картинку"
    )
    link_to_video = models.CharField(
        max_length=200,
        **NULLABLE,
        verbose_name="ссылка на видео",
        help_text="Добавьте ссылку на видео"
    )

    course = models.ForeignKey(
        Course,
        **NULLABLE,
        on_delete=models.SET_NULL,
        verbose_name="курс",
        help_text="Выберите курс"
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, **NULLABLE,
        verbose_name="владелец")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
        ordering = ("title",)
