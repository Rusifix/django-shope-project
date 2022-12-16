from users.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
from django.core.paginator import Paginator
# Create your views here.
# функция = контроллеры = вьюхи
def index(requets):
    context = {
        'title': 'Store',
        'is_promotion': False,
    }
    return render(requets, 'products/index.html', context)

def products(request, category_id=None, page=1):

    product = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(product, per_page)
    products_paginator = paginator.page(page)
    context = {
        'title': 'Store-Каталог',
        'products': products_paginator,
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)

@login_required()
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantite=1)
    else:
        baskets = baskets.first()
        baskets.quantite += 1
        baskets.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required()
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
