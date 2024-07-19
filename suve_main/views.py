from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .models import Product, Routes


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
        'brand_page': product
    }
    return render(request, 'suve_main/products/products.html', context=data)


def products(request, brands):
    product = Product.objects.filter(brand=brands)
    data = {
        'brand': brands,
        'products': product
    }
    return render(request, f'suve_main/products/product_{brands.lower()}/product_{brands.lower()}.html', context=data)


def contacts_page(request):
    urls = Routes.objects.all()
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/contacts/contacts.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('try again')
