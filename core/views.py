from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import get_user_model
from product.models import product, ProductImage
from accounts.models import Store
from order.models import Order

def index(request):
    if request.user.is_authenticated:
        store = None
        Product = None
        Checkout = None
        try:
            store = Store.objects.get(seller_id = request.user)
            Checkout = Order.objects.filter(buyer_id = request.user).order_by('-created_at')
            Product = product.objects.all()
        except (Store.DoesNotExist, Order.DoesNotExist):
            Product = product.objects.all()
            
        return render(request,'index.html', {'Product' : Product, 'Store' : store, 'Checkout' : Checkout})
    else:
        return redirect('signin')