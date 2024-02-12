from django.urls import path
from .views import OrderView,OrderNextView,detailorder,orderflow,storeorderflow

urlpatterns = [
    path("order-product/<Product>", OrderView, name="orderproduct"),
    path("order-product/<Product>/next/", OrderNextView, name="cekjson"),
    path("order-product/detail-lorder/<order_id>/", detailorder, name="detailorder"),
    path("order-product/<order_id>/order-flow/", orderflow, name="orderflow"),
    path("order-product/<order_id>/store-order-flow/", storeorderflow, name="storeorderflow"),
]
    