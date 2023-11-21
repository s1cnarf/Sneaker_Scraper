from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Offer


# Create your views here.
def home(request):
    items = Product.objects.all()
    
    context  = {'items':items}
    
    return render(request, 'main.html', context)

