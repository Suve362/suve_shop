from django.db import models
from django.urls import reverse


class Routes(models.Model):
    url_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['id']
        verbose_name_plural = "Routes"

    def __str__(self):
        return self.name


class Login(models.Model):
    email = models.CharField(max_length=255, verbose_name='Email')
    password = models.CharField(max_length=255, verbose_name='Password')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Time')

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['date']
        verbose_name = "Login"
        verbose_name_plural = "Login"


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='PRODUCT NAME')
    brand = models.CharField(max_length=255, verbose_name='BRAND')
    category = models.CharField(max_length=255, verbose_name='CATEGORY')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['brand', 'category']
        verbose_name = "Product"
        verbose_name_plural = "Products"

    # def get_absolute_url(self):
    #     return reverse('products_page', kwargs={'slug': self.brand})


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/', default=None, blank=True, null=True, verbose_name='PHOTO')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name='PRODUCT')

    class Meta:
        verbose_name = "Product Photo"
        verbose_name_plural = "Product Photo"

    def __str__(self):
        return str(self.product)


class StorageSpecs(models.Model):
    rom = models.IntegerField(verbose_name='ROM')
    ram = models.IntegerField(blank=True, null=True, verbose_name='RAM')
    cpu = models.CharField(max_length=255, blank=True, null=True, verbose_name='CPU')
    gpu = models.CharField(max_length=255, blank=True, null=True, verbose_name='GPU')
    diagonal = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True, verbose_name='Diagonal')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='PRODUCT')

    class Meta:
        verbose_name = "Storage Spec"
        verbose_name_plural = "Storage Specs"

    def __str__(self):
        return str(self.product)


class WatchSpecs(models.Model):
    size = models.IntegerField(verbose_name='SIZE')
    material = models.CharField(max_length=255, verbose_name='MATERIAL')
    connectivity = models.CharField(max_length=255, blank=True, null=True, verbose_name='CONNECTIVITY')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='PRODUCT')

    class Meta:
        verbose_name = "Watch Spec"
        verbose_name_plural = "Watch Specs"

    def __str__(self):
        return str(self.product)


class CarSpecs(models.Model):
    type = models.CharField(max_length=255, verbose_name='TYPE')
    extra_options = models.BooleanField(blank=True, null=True, verbose_name='EXTRA OPTIONS')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='PRODUCT')

    class Meta:
        verbose_name = "Car Spec"
        verbose_name_plural = "Car Specs"

    def __str__(self):
        return self.type


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='PRODUCT')
    storage_spec = models.ForeignKey(StorageSpecs, on_delete=models.CASCADE, blank=True, null=True,
                                     verbose_name='STORAGE SPEC ID', related_name='storage_spec')
    watch_spec = models.ForeignKey(WatchSpecs, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='WATCH SPEC ID', related_name='watch_spec')
    car_spec = models.ForeignKey(CarSpecs, on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='CAR SPEC ID', related_name='car_spec')
    price = models.IntegerField()

    class Meta:
        verbose_name = "Product Price"
        verbose_name_plural = "Product Prices"

    def __str__(self):
        return str(self.product)







