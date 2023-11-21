import uuid
import os
from urllib.parse import urlparse
from django.db import models
# Create your models here.

class Offer(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False) 
    type = models.CharField(max_length=200)
    lowPrice = models.DecimalField(decimal_places=2, max_digits=6)
    highPrice = models.DecimalField(decimal_places=2, max_digits=6)
    priceCurrency = models.CharField(max_length=50)
    offer_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    type =  models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=200, null=True)
    itemcondition = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    releaseDate = models.DateTimeField(auto_now=True)
    sku = models.UUIDField(unique=True)
    product_url = models.URLField(max_length=200)

    offers = models.ForeignKey(Offer, on_delete=models.CASCADE)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

