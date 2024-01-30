from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import get_user_model
from product.models import product, ProductImage
from accounts.models import Store

def index(request):
    if request.user.is_authenticated:
        store = None
        Product = None
        try:
            store = Store.objects.get(store_seller_id = request.user)
            Product = product.objects.all()
        except Store.DoesNotExist:
            Product = product.objects.all()
            
        return render(request,'index.html', {'Product' : Product})
    else:
        return redirect('signin')