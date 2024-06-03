from django.db import models

from users.models import NULLABLE


class Course(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='Укажите название курса'
    )
    description = models.TextField(
        verbose_name='описание', **NULLABLE,
        help_text='Укажите описание курса'
    )
    picture = models.ImageField(
        upload_to='lms/pictures', **NULLABLE,
        verbose_name='превью (картинка)',
        help_text='Загрузите картинку'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
        ordering = ('title',)


class Lesson(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='название',
        help_text='Укажите название урока'
    )
    description = models.TextField(
        verbose_name='описание', **NULLABLE,
        help_text='Укажите описание урока'
    )
    picture = models.ImageField(
        upload_to='lms/pictures', **NULLABLE,
        verbose_name='превью (картинка)',
        help_text='Загрузите картинку'
    )
    link_to_video = models.CharField(
        max_length=200, **NULLABLE,
        verbose_name='ссылка на видео',
        help_text='Добавьте ссылку на видео'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
        ordering = ('title',)