from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound

from .forms import ProductForm
from .models import *


# def handle_uploaded_file(f):
#     with open(f'uploads/{f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def main_page(request):
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            fp = ProductPhoto(photo=form.cleaned_data['photo'])
            fp.save()
            return redirect('main')
    else:
        form = ProductForm()
    data = {
        'routes': urls,
        'form': form
    }
    return render(request, 'suve_main/main/main.html', context=data)


def pages(request, page_id):
    if page_id == 1:
        return redirect('main')
    return HttpResponse(f'this is {page_id}')


def main(request):
    return redirect('main')


def login(request):
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/login/login.html', context=data)


def contacts_page(request):
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/contacts/contacts.html', context=data)


def cart_page(request):
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    data = {
        'routes': urls
    }
    return render(request, 'suve_main/cart/cart.html', context=data)


def products_page(request):
    product = Product.objects.all()
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    data = {
        'routes': urls,
        'brand_page': product,
    }
    return render(request, 'suve_main/products/products.html', context=data)


def products_apple(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_apple/product_apple.html', context=data)


def products_apple_iphone(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple", category="smartphone")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_apple/product_apple_iphone/product_apple_iphone.html', context=data)


def products_apple_ipad(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple", category="tablet")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_apple/product_apple_ipad/product_apple_ipad.html', context=data)


def products_apple_macbook(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple", category="laptop")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_apple/product_apple_macbook/product_apple_macbook.html', context=data)


def products_apple_mac(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple", category="pc")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_apple/product_apple_mac/product_apple_mac.html', context=data)


def products_apple_watch(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple", category="smartwatch")
    product_data = []

    for product in products:
        watch_specs = WatchSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for watch_spec in watch_specs:
            price = get_object_or_404(ProductPrice, product=product, watch_spec=watch_spec)
            product_data.append({
                'product_id': product.id,
                'watch_spec_id': watch_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'size': watch_spec.size,
                'material': watch_spec.material,
                'connectivity': watch_spec.connectivity,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_apple/product_apple_watch/product_apple_watch.html',
                  context=data)


def products_apple_airpods(request):
    urls = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
    products = Product.objects.filter(brand="apple", category="headphones")
    product_data = []

    for product in products:
        products_photo = ProductPhoto.objects.filter(product=product).first()
        price = get_object_or_404(ProductPrice, product=product)
        product_data.append({
            'product_id': product.id,
            'name': product.name,
            'brand': product.brand,
            'category': product.category,
            'price': price.price,
            'photo': products_photo.photo.url
        })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_apple/product_apple_airpods/product_apple_airpods.html',
                  context=data)


def products_samsung(request):
    urls = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
    products = Product.objects.filter(brand="samsung")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_samsung/product_samsung.html', context=data)


def products_samsung_smartphones(request):
    urls = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
    products = Product.objects.filter(brand="samsung", category="smartphone")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_samsung/product_samsung_smartphone/product_samsung_smartphone.html',
                  context=data)


def products_samsung_tab(request):
    urls = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
    products = Product.objects.filter(brand="samsung", category="tablet")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_samsung/product_samsung_tab/product_samsung_tab.html',
                  context=data)


def products_samsung_galaxybook(request):
    urls = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
    products = Product.objects.filter(brand="samsung", category="laptop")
    product_data = []

    for product in products:
        storage_specs = StorageSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for storage_spec in storage_specs:
            price = get_object_or_404(ProductPrice, product=product, storage_spec=storage_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': storage_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'rom': storage_spec.rom,
                'ram': storage_spec.ram,
                'cpu': storage_spec.cpu,
                'diagonal': storage_spec.diagonal,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_samsung/product_samsung_galaxybook/product_samsung_galaxybook.html',
                  context=data)


def products_samsung_watch(request):
    urls = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
    products = Product.objects.filter(brand="samsung", category="smartwatch")
    product_data = []

    for product in products:
        watch_specs = WatchSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for watch_spec in watch_specs:
            price = get_object_or_404(ProductPrice, product=product, watch_spec=watch_spec)
            product_data.append({
                'product_id': product.id,
                'watch_spec_id': watch_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'size': watch_spec.size,
                'material': watch_spec.material,
                'connectivity': watch_spec.connectivity,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_samsung/product_samsung_watch/product_samsung_watch.html',
                  context=data)


def products_samsung_galaxybuds(request):
    urls = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
    products = Product.objects.filter(brand="samsung", category="headphones")
    product_data = []

    for product in products:
        products_photo = ProductPhoto.objects.filter(product=product).first()
        price = get_object_or_404(ProductPrice, product=product)
        product_data.append({
            'product_id': product.id,
            'name': product.name,
            'brand': product.brand,
            'category': product.category,
            'price': price.price,
            'photo': products_photo.photo.url
        })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request,
                  f'suve_main/products/product_samsung/product_samsung_galaxybuds/product_samsung_galaxybuds.html',
                  context=data)


def products_tesla(request):
    urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    products = Product.objects.filter(brand="tesla")
    product_data = []

    for product in products:
        car_specs = CarSpecs.objects.filter(product=product)
        products_photo = ProductPhoto.objects.filter(product=product).first()
        for car_spec in car_specs:
            price = get_object_or_404(ProductPrice, product=product, car_spec=car_spec)
            product_data.append({
                'product_id': product.id,
                'storage_spec_id': car_spec.id,
                'name': product.name,
                'brand': product.brand,
                'category': product.category,
                'type': car_spec.type,
                'price': price.price,
                'photo': products_photo.photo.url
            })

    data = {
        'product_data': product_data,
        'routes': urls
    }
    return render(request, f'suve_main/products/product_tesla/product_tesla.html', context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound('try again')
