from django.core.management.base import BaseCommand
import json
import os
from mainapp.models import Product, Category


JSON_PATH = 'mainapp/jsons'


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r', encoding='UTF-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        products = load_from_json('products')

        Category.objects.all().delete()
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        Product.objects.all().delete()
        for product in products:
            product['category'] = Category.objects.get(pk=product['category'])
            new_product = Product(**product)
            new_product.save()

