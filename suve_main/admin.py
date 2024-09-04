from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category')
    list_display_links = ('name',)
    list_per_page = 100
    search_fields = ('name',)
    list_filter = ('category', 'brand')
    fields = ('name', 'brand', 'category')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'eur_price', 'byn_price', 'storage_spec_id', 'watch_spec_id',
                    'car_spec_id')
    list_display_links = ('product',)
    list_editable = ('price',)
    list_per_page = 400
    search_fields = ('product__name',)

    @admin.display(description='EUR Price')
    def eur_price(self, product: ProductPrice):
        return f'{round(product.price * 0.92, 2)}'

    @admin.display(description='BYN Price')
    def byn_price(self, product: ProductPrice):
        return f'{round(product.price * 3.12, 2)}'


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'photo', 'photo_image')
    list_display_links = ('product',)
    list_editable = ('photo',)
    list_per_page = 100
    search_fields = ('product__name',)

    @admin.display(description='IMAGE')
    def photo_image(self, product: ProductPhoto):
        if product.photo:
            return mark_safe(f'<img src="{product.photo.url}" width=20%>')
        return 'No photo'


@admin.register(StorageSpecs)
class StorageSpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'rom', 'ram', 'cpu', 'gpu', 'diagonal')
    list_display_links = ('product',)
    list_editable = ('rom', 'ram', 'cpu', 'gpu', 'diagonal')
    list_per_page = 400
    search_fields = ('product__name',)
    list_filter = ('rom', 'ram', 'cpu', 'gpu', 'diagonal')
    fields = ('product', 'rom', 'ram', 'cpu', 'gpu', 'diagonal')


@admin.register(WatchSpecs)
class WatchSpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'size', 'material', 'connectivity')
    list_display_links = ('product',)
    list_editable = ('size', 'material', 'connectivity')
    list_per_page = 400
    search_fields = ('product__name',)
    list_filter = ('size', 'material', 'connectivity')
    fields = ('product', 'size', 'material', 'connectivity')


@admin.register(CarSpecs)
class CarSpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'type', 'extra_options')
    list_display_links = ('product',)
    list_editable = ('type', 'extra_options')
    list_per_page = 100
    search_fields = ('product__name',)
    list_filter = ('type', 'extra_options')
    fields = ('product', 'type', 'extra_options')


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_name')
    list_editable = ('name', 'url_name')
    list_per_page = 50
    search_fields = ('name',)



