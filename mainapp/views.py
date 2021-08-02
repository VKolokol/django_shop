import json

from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from basketapp.models import Basket


# Create your views here.


def get_context(request):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    category = Category.objects.all()
    products = Product.objects.all()

    return {
        'product': products,
        'categories': category,
        'basket':basket,
    }


def index_view(request):

    return render(request, 'index.html', context=get_context(request))


def contacts_view(request):
    return render(request, 'contacts.html', context=get_context(request))


def catalog_view(request, slug=None):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if slug is not None:
        if slug == 'all':
            return render(request, 'collection.html', context=get_context(request))
        if get_object_or_404(Category, slug=slug):
            context = get_context(request)
            context['product'] = Product.objects.all().filter(category__slug=slug)
            return render(request, 'collection.html', context=context)



