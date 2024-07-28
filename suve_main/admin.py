from django.contrib import admin
from .models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'category')


@admin.register(ProductPrice)
class ProductPriceAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price')


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'photo')


@admin.register(StorageSpecs)
class StorageSpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'rom', 'ram', 'cpu', 'gpu', 'diagonal')


@admin.register(WatchSpecs)
class WatchSpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'size', 'material', 'connectivity')


@admin.register(CarSpecs)
class CarSpecsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'type', 'extra_options')


@admin.register(Routes)
class RoutesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url_name')



