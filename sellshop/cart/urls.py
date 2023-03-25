from django.urls import path
from . import views


urlpatterns = [
    path('wishlist', views.wishlist, name='wishlist'),
    path('order-complete', views.order_complete, name='order_complete')

    ]
