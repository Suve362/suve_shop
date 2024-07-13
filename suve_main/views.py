from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

routes = [
    {'title': 'Log in', 'url_name': 'login'},
    {'title': 'Cart', 'url_name': 'cart'},
    {'title': 'Main', 'url_name': 'main'},

]


def main_page(request):
    data = {'routes': routes}
    return render(request, 'suve_main/main/main.html', context=data)


def pages(request, page_id):
    if page_id == 1:
        return redirect('main')
    return HttpResponse(f'this is {page_id}')


def login(request):
    data = {'routes': routes}
    return render(request, 'suve_main/login/login.html', context=data)


def cart(request):
    data = {'routes': routes}
    return render(request, 'suve_main/cart/cart.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('try again')
