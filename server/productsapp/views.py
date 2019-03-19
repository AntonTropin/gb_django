from django.shortcuts import render

# Create your views here.

def product_list(requiest):
    return render(requiest, 'productsapp/product_list.html')

def product_detail(requiest):
    return render(requiest, 'productsapp/product_detail.html')

