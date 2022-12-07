from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Products


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'create_at', 'get_image']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width='100' height='110'")
        return mark_safe(f"<img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS510QHadvt5K0mPhT0_Myiuu-KoCYPP0pexOUuxzLacA&s' width='100' height='110'")


admin.site.register(Products, ProductsAdmin)