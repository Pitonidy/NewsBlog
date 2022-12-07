from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текс')
    image = models.ImageField(upload_to='news/', verbose_name='Картинка')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    created_at = models.DateTimeField(auto_created=True, verbose_name='Дата создание')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

