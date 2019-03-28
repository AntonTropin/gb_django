from django.shortcuts import render
from .models import Category, Type, Product

# Create your views here.

def product_list(requiest, pk):
    return render(
        requiest, 
        'productsapp/product_list.html',
        {
            'categorys' : Category.objects.get(id=pk), 
            'types' : Type.objects.get(category=pk),
        }
    )

def product_detail(requiest):
    return render(requiest, 'productsapp/product_detail.html')

