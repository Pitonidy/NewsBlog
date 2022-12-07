from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Products


# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'photo']

    def photo(self, obj):
        if obj.image
            return mark_safe(f"<img src = {obj.image.url} width = '20%'>")
        else:
            return None

admin.site.register(Products, ProductsAdmin)
