from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('product/<str:id>', views.index_id, name='product'),
    path('about', views.index, name='about'),
    path('contact', views.index, name='contact'),
    path('checkout', views.index, name='validation'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'backend.views.error404'