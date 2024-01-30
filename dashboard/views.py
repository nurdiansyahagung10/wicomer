from django.shortcuts import render
from accounts.models import Store
from product.models import product
# Create your views here. 

def dashboard_store(request):
    store = Store.objects.get(store_seller_id = request.user)
    Product = product.objects.filter(store_id = store)
    return render(request, 'dashboard/store_dashboard.html', {'store':store, 'product': Product})

