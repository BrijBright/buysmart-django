from django.contrib import admin
from .models import Product, Variation, ReviewRating, ProductGallery
from django.utils.html import format_html


class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1
    readonly_fields = ('product_name', 'preview_image')
    fields = ('product_name', 'image', 'preview_image')
    can_delete = False

    def product_name(self, instance):
        return instance.product.product_name
    
    def preview_image(self, instance):
        if instance.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', instance.image.url)
        return 'No Image'
    preview_image.short_description = 'Image Preview'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'is_available', 'preview_image')
    prepopulated_fields = {'slug': ('product_name',)}
    inlines = [ProductGalleryInline]

    def preview_image(self, obj):
        if obj.images:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.images.url)
        return 'No Image'
    preview_image.short_description = 'Preview Image'
    preview_image.allow_tags = True


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'product_image')
    list_editable = ('is_active',)
    list_filter = ('product', 'variation_category', 'variation_value')

    def product_image(self, obj):
        if obj.product.images:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.product.images.url)
        return 'No Image'
    product_image.short_description = 'Product Image'
    product_image.allow_tags = True


class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_preview')

    def image_preview(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery, ProductGalleryAdmin)
