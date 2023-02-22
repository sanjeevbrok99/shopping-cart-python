from django.urls import path
from .views import ShoppingCart

urlpatterns = [
    path('cart-items/', ShoppingCart.as_view()),
]