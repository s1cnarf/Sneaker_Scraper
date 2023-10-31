from django.contrib import admin

# Register your models here.
from .models import Offer, Product

admin.site.register(Offer)
admin.site.register(Product)    