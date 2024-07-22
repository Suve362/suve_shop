from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import *


def main_page(request):
    urls = Routes.objects.all()
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/main/main.html', context=data)


def pages(request, page_id):
    if page_id == 1:
        return redirect('main')
    return HttpResponse(f'this is {page_id}')


def main(request):
    return redirect('main')


def login(request):
    urls = Routes.objects.all()
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/login/login.html', context=data)


def cart_page(request):
    urls = Routes.objects.all()
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/cart/cart.html', context=data)


def products_page(request):
    product = Product.objects.all()
    urls = Routes.objects.all()
    data = {
        'routes': urls,
        'brand_page': product,
    }
    return render(request, 'suve_main/products/products.html', context=data)


def products_apple(request):
    products = Product.objects.filter(brand="apple")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'diagonal': storage_spec.diagonal,
                'price': price.price
            })

    data = {
        'product_data': product_data
    }
    return render(request, f'suve_main/products/product_apple/product_apple.html', context=data)


def products_samsung(request):
    products = Product.objects.filter(brand="samsung")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'diagonal': storage_spec.diagonal,
                'price': price.price
            })

    data = {
        'product_data': product_data
    }
    return render(request, f'suve_main/products/product_samsung/product_samsung.html', context=data)


def products_tesla(request):
    products = Product.objects.filter(brand="tesla")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'diagonal': storage_spec.diagonal,
                'price': price.price
            })

    data = {
        'product_data': product_data
    }
    return render(request, f'suve_main/products/product_tesla/product_tesla.html', context=data)


def contacts_page(request):
    urls = Routes.objects.all()
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/contacts/contacts.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('try again')
