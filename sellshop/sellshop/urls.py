from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from products.views import *
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('', include('accounts.urls')),
    path('', include('cart.urls')),
    path('', include('pages.urls'))
               ] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

    