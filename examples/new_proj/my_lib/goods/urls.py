from django.urls import path
from .views import get_products, set_current_amount_products

urlpatterns = [
    path('get_products/', get_products),
    path('set_current_amount_products/', set_current_amount_products),
]

