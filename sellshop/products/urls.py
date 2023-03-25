from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.products, name='products'),
    path('single/', views.single_product, name='single_product')
    
]
