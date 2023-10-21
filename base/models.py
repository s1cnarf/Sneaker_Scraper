from django.db import models

# Create your models here.

class Offer(models.Model):
    type = models.CharField(max_length=200)
    lowPrice = models.DecimalField(decimal_places=2, max_digits=6)
    highPrice = models.DecimalField(decimal_places=2, max_digits=6)
    priceCurrency = models.CharField(max_length=50)
    offer_url = models.URLField(max_length=200)

class Product(models.Model):
    type =  models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="path/filename" )
    itemcondition = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    releaseDate = models.DateTimeField(auto_now=True)
    sku = models.UUIDField(unique=True)
    product_url = models.URLField(max_length=200)

    offers = models.ForeignKey(Offer, on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

