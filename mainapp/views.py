import json

from django.shortcuts import render

# Create your views here.


products = [
    {'id': 1, 'category': 'vinyl', 'title': 'Led Zeppelin 2', 'price': 2000},
    {'id': 2, 'category': 'vinyl', 'title': 'Led Zeppelin 3', 'price': 4000},
    {'id': 3, 'category': 'cd_disk', 'title': 'Korn Issues', 'price': 500},
    {'id': 4, 'category': 'cd_disk', 'title': 'Korn Follow the Leader', 'price': 600},
    {'id': 5, 'category': 'player', 'title': 'Audio-Technica AT-LPW30', 'price': 29000},
    {'id': 6, 'category': 'player', 'title': 'LSony PS-HX500', 'price': 36000}
]



def index_view(request):
    return render(request, 'index.html')


def contacts_view(request):
    return render(request, 'contacts.html')


def catalog_view(request):
    content = {'product': products}
    return render(request, 'collection.html', context=content)
