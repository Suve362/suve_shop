from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.views import View
from django.views.generic import TemplateView, CreateView, ListView

# from .forms import LoginForm
# from .forms import ProductForm
from .models import *
from .utils import ProductMixin


# def handle_uploaded_file(f):
#     with open(f'uploads/{f.name}', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


class MainPage(TemplateView):
    template_name = 'suve_main/main/main.html'
    # extra_context = {
    #     'routes': Routes.objects.filter(pk__in=[1, 2, 3, 4]),
    # }


# def pages(request, page_id):
#     if page_id == 1:
#         return redirect('main')
#     return HttpResponse(f'this is {page_id}')


def main(request):
    return redirect('main')


# class Login(CreateView):
#     form_class = LoginForm
#     template_name = 'suve_main/login/login.html'
#     urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
#     extra_context = {
#         'routes': urls,
#     }
#     # if request.method == 'POST':
#     #     form = LoginForm(request.POST, request.FILES)
#     #     if form.is_valid():
#
#     def form_valid(self, form):
#         form.save()
#         return redirect('main')


class ContactsPage(TemplateView):
    template_name = 'suve_main/contacts/contacts.html'
    # urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    # extra_context = {
    #     'routes': urls
    # }


class CartPage(TemplateView):
    template_name = 'suve_main/cart/cart.html'
    # urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    # extra_context = {
    #     'routes': urls
    # }


class ProductsPage(ListView):
    model = Product
    template_name = 'suve_main/products/products.html'
    # urls = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    # extra_context = {
    #     'routes': urls,
    # }

    def get_queryset(self):
        pass


class ProductsApple(LoginRequiredMixin, ProductMixin, ListView):
    template_name = 'suve_main/products/product_apple/product_apple.html'
    context_object_name = 'product_data'

    def get_queryset(self):
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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsAppleIphone(ProductMixin, ListView):

    template_name = 'suve_main/products/product_apple/product_apple_iphone/product_apple_iphone.html'
    context_object_name = 'product_data'

    def get_queryset(self):
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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsAppleIpad(ProductMixin, ListView):

    template_name = 'suve_main/products/product_apple/product_apple_ipad/product_apple_ipad.html'
    context_object_name = 'product_data'

    def get_queryset(self):
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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsAppleMacbook(ProductMixin, ListView):

    template_name = 'suve_main/products/product_apple/product_apple_macbook/product_apple_macbook.html'
    context_object_name = 'product_data'

    def get_queryset(self):
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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsAppleMac(ProductMixin, ListView):

    template_name = 'suve_main/products/product_apple/product_apple_mac/product_apple_mac.html'
    context_object_name = 'product_data'

    def get_queryset(self):
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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsAppleWatch(ProductMixin, ListView):

    template_name = 'suve_main/products/product_apple/product_apple_watch/product_apple_watch.html'
    context_object_name = 'product_data'

    def get_queryset(self):
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

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsAppleAirpods(ProductMixin, ListView):

    template_name = 'suve_main/products/product_apple/product_apple_airpods/product_apple_airpods.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 5, 6, 7, 14, 16, 17]).order_by("id")
        return context


class ProductsSamsung(LoginRequiredMixin, ProductMixin, ListView):

    template_name = 'suve_main/products/product_samsung/product_samsung.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
        return context


class ProductsSamsungSmartphones(ProductMixin, ListView):

    template_name = 'suve_main/products/product_samsung/product_samsung_smartphone/product_samsung_smartphone.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
        return context


class ProductsSamsungTab(ProductMixin, ListView):

    template_name = 'suve_main/products/product_samsung/product_samsung_tab/product_samsung_tab.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
        return context


class ProductsSamsungGalaxybook(ProductMixin, ListView):

    template_name = 'suve_main/products/product_samsung/product_samsung_galaxybook/product_samsung_galaxybook.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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
                    'gpu': storage_spec.gpu,
                    'diagonal': storage_spec.diagonal,
                    'price': price.price,
                    'photo': products_photo.photo.url
                })

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
        return context


class ProductsSamsungWatch(ProductMixin, ListView):

    template_name = 'suve_main/products/product_samsung/product_samsung_watch/product_samsung_watch.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
        return context


class ProductsSamsungGalaxybuds(ProductMixin, ListView):

    template_name = 'suve_main/products/product_samsung/product_samsung_galaxybuds/product_samsung_galaxybuds.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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

        return product_data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['routes'] = Routes.objects.filter(pk__in=[1, 8, 9, 10, 12, 13, 18]).order_by("id")
        return context


class ProductsTesla(LoginRequiredMixin, ProductMixin, ListView):
    template_name = 'suve_main/products/product_tesla/product_tesla.html'
    context_object_name = 'product_data'

    def get_queryset(self):

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

        return product_data

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['routes'] = Routes.objects.filter(pk__in=[1, 2, 3, 4])
    #     return context


def page_not_found(request, exception):
    return HttpResponseNotFound('try again')
