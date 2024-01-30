from django.shortcuts import render
from product.models import product

def OrderView(request, Product):
    data = product.objects.get(name_product = Product)
    return render(request, 'order/order.html', {'Product' : data})
