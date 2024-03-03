from django.contrib import admin
from .models import Category
from django.utils.html import format_html


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug', 'cat_image_preview')

    def cat_image_preview(self, obj):
        if obj.cat_image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.cat_image.url)
        return 'No Image'
    cat_image_preview.short_description = 'Category Image'


admin.site.register(Category, CategoryAdmin)
