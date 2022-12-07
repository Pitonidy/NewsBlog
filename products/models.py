from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    description = models.TextField(verbose_name='Характеристика', null=True, blank=True)
    price = models.IntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Фото товара', blank=True)
    category = models.CharField(max_length=255, verbose_name='Категория', blank=True)
    #data_create = datetime()
    expire_date = models.DateField(verbose_name='Срок годности')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавление')
    made_in = models.CharField(max_length=255, verbose_name='Страна производитель')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
