from django.shortcuts import render
from accounts.models import Store
from product.models import product
from order.models import Order
# Create your views here. 

def dashboard_store(request):
    store = Store.objects.get(seller_id = request.user)
    Product = product.objects.filter(store_id = store)
    order = Order.objects.filter(store_id = store) 
    return render(request, 'dashboard/store_dashboard.html', {'store':store, 'product': Product,'order': order})

