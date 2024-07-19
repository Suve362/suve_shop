from django.db import models
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-brand']

    def get_absolute_url(self):
        return reverse('products', kwargs={'slug': self.brand})


class Routes(models.Model):
    url_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50, unique=True)




