from django.urls import path
from . import views


urlpatterns = [
    path('getProducts', views.getProducts, name='products_api'),
    path('getProduct/<str:id>', views.getProduct, name='getProduct_byId'),
    path('validateBag', views.validateBag, name='validateBag_api'),
    path('subscribe', views.subscribe, name='subscribe_to_newsletter'),
    path('contact', views.contact, name='contact'),
    path('get-csrf-token/', views.get_csrf_token),
]