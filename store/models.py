from django.db import models

import shortuuid
from djmoney.models.fields import MoneyField


# Create your models here.


class Product(models.Model):
    year = models.IntegerField()
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    horsepower = models.IntegerField()
    engine = models.CharField(max_length=100)
    stock_number = models.CharField(max_length=100, default=shortuuid.ShortUUID().random(length=6))
    price = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    image = models.ImageField(upload_to='upload/products')
    image1 = models.ImageField(upload_to='upload/products', blank=True, null=True)
    image2 = models.ImageField(upload_to='upload/products', blank=True, null=True)
    image3 = models.ImageField(upload_to='upload/products', blank=True, null=True)
    image4 = models.ImageField(upload_to='upload/products', blank=True, null=True)

    def __str__(self):
        return f'{self.year} {self.make} {self.model}'


from django.db import models

# Create your models here.
