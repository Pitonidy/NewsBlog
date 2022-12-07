from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image', 'author', 'create_at']

    def get_image(self, obj):
        return mark_safe(f"<img src={obj.image.url} width='100' height='100'")


admin.site.register(News, NewsAdmin)
