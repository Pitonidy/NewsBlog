from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Фото', blank=True, null=True)
    category = models.CharField(max_length=255, verbose_name='Категория', blank=True, null=True)
    data_create = models.DateTimeField(verbose_name='Дата выпуска')
    expire_date = models.DateTimeField(verbose_name='Срок годности')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания записи')
    made_in = models.CharField(max_length=255, verbose_name='Произведено')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-create_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
