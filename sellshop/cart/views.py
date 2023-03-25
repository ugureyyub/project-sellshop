from django.shortcuts import render

def wishlist(request):
    return render(request, 'cart/wishlist.html' )


def order_complete(request):
    return render(request, 'cart/order-complete.html' )
