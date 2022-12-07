from django.contrib.auth.models import User
from django.db import models


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Текст')
    image = models.ImageField(upload_to='news/', verbose_name='Изображение')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['create_at']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
