from django.shortcuts import render
from .models import Category, Type, Product

# Create your views here.

def product_list(requiest, pk):
    return render(
        requiest, 
        'productsapp/product_list.html',
        {
            'categorys' : Category.objects.all(), 
            'types' : Type.objects.all(),
            'product' : Product.objects.all(),
        }
    )

def product_detail(requiest):
    return render(requiest, 'productsapp/product_detail.html')

