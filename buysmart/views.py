from django.shortcuts import render
from store.models import Product
import random

def home(request):
    # Retrieve all products that are available
    available_products = Product.objects.filter(is_available=True)

    # Shuffle the available products to get a random order
    random_products = random.sample(list(available_products), min(8, len(available_products)))

    context = {
        'products': random_products,
    }
    return render(request, 'home.html', context)
