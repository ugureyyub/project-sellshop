from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('my_account/', views.my_account, name='my-account')

    
]
