from django.shortcuts import render
from .models import *
from datetime import date
from apps.offers.models import Offer

# Create your views here.


def products_card(request):
    categories=Category.objects.all()
    offers = Offer.objects.all()
    cart = []
    for category in categories:
       cart.append({
           'category': category.category_name,
           'products': Product.objects.filter(category=category).exclude(active=False)
       })
    contexto = {'cart': cart, 'categories': categories, 'offers':offers}
    return render(request,'index.html',contexto)