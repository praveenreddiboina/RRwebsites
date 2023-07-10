
from django.urls import path
from .views import *


urlpatterns = [
     path('', Index.as_view(), name='homepage'),
     path('store', store , name='store'),
     path('about', about, name='about'),
     path('products',products, name='products'),
     path('contact', contact, name="contact"),
]