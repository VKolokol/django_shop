import json

from django.shortcuts import render
from .models import Product
# Create your views here.





def index_view(request):
    return render(request, 'index.html')


def contacts_view(request):
    return render(request, 'contacts.html')


def catalog_view(request):
    products = Product.objects.all()
    content = {'product': products}
    return render(request, 'collection.html', context=content)
