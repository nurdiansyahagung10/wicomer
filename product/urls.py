from django.urls import path
from .views import createproduct

urlpatterns = [
    path("create-product/", createproduct, name="createproduct")
]
    