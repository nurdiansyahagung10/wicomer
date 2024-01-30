from django.urls import path
from .views import OrderView

urlpatterns = [
    path("order-product/<Product>", OrderView, name="orderproduct")
]
    