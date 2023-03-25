from django.shortcuts import render

def products(request):
    return render(request, 'products/product-list.html' )


def single_product(request):
    return render(request, 'products/single-product.html' )

