from django.urls import path
from . import views


urlpatterns = [
    path('single-blog/', views.single_blog, name='single_blog'),
    
]
