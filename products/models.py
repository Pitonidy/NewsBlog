from django.contrib.auth.models import User
from django.db import models


class Products(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    descriptions = models.TextField(verbose_name='Описание')
    price = models.PositiveIntegerField(verbose_name='Цена')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    category = models.CharField(max_length=255, verbose_name='Категория')
    data_create = models.DateField(verbose_name='Дата изготовления')
    expire_date = models.DateField(verbose_name='Срок годности')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания поста')
    made_in = models.CharField(max_length=100, verbose_name='Место изготовления')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', 'create_at']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
