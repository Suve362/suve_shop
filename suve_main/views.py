from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

routes = [
    {'url_name': 'main', 'name': 'Main'},
    {'url_name': 'products', 'name': 'Products'},
    {'url_name': 'contacts', 'name': 'Contacts'},
    {'url_name': 'cart', 'name': 'Cart'},
]


def main_page(request):
    data = {'routes': routes}
    return render(request, 'suve_main/main/main.html', context=data)


def pages(request, page_id):
    if page_id == 1:
        return redirect('main')
    return HttpResponse(f'this is {page_id}')


def main(request):
    return redirect('main')


def login(request):
    data = {'routes': routes}
    return render(request, 'suve_main/login/login.html', context=data)


def cart_page(request):
    data = {'routes': routes}
    return render(request, 'suve_main/cart/cart.html', context=data)


def products_page(request):
    data = {'routes': routes}
    return render(request, 'suve_main/products/products.html', context=data)


def contacts_page(request):
    data = {'routes': routes}
    return render(request, 'suve_main/contacts/contacts.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('try again')
