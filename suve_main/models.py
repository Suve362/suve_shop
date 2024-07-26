from django.db import models
from django.urls import reverse


class Routes(models.Model):
    url_name = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Product_name')
    brand = models.CharField(max_length=255, verbose_name='Brand')
    category = models.CharField(max_length=255, verbose_name='Category')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-brand']

    def get_absolute_url(self):
        return reverse('products_page', kwargs={'slug': self.brand})


class ProductPhoto(models.Model):
    photo = models.ImageField(upload_to='photos/', default=None, blank=True, null=True, verbose_name='Photo')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)


class StorageSpecs(models.Model):
    rom = models.IntegerField()
    ram = models.IntegerField(blank=True, null=True)
    cpu = models.CharField(max_length=255, blank=True, null=True)
    gpu = models.CharField(max_length=255, blank=True, null=True)
    diagonal = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class WatchSpecs(models.Model):
    size = models.IntegerField()
    material = models.CharField(max_length=255)
    connectivity = models.CharField(max_length=255, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class CarSpecs(models.Model):
    type = models.CharField(max_length=255)
    extra_options = models.BooleanField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class ProductPrice(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    storage_spec = models.ForeignKey(StorageSpecs, on_delete=models.CASCADE, blank=True, null=True)
    watch_spec = models.ForeignKey(WatchSpecs, on_delete=models.CASCADE, blank=True, null=True)
    car_spec = models.ForeignKey(CarSpecs, on_delete=models.CASCADE, blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return str(self.price)







