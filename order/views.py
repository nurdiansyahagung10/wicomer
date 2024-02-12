from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from product.models import product,ProductImage
from accounts.models import Address
from .models import Order
from django.contrib.auth import get_user_model 
from django.utils import timezone

def OrderView(request,Product):
    value_product = get_object_or_404(product, name_product = Product)     

    if request.method == 'POST':    
        spesification = ''
        spesificationvalue = ''

        for val_spesification in request.POST.getlist('spesification'):
            spesification += str(val_spesification + ',')      
            listname = str(val_spesification + 'value')
            for val_valuespesification in request.POST.getlist(listname):
                spesificationvalue += str(val_valuespesification + ',')        
        address = Address.objects.get(user_id = request.user)

        jsondata = {
            "buyer" : request.user.username,
            "address" : address.id,
            "quantity" : request.POST.get('qty'),
            "product" : value_product.name_product,
            "price" : request.POST.get('price'),
            "spesification" : spesification,
            "spesificationvalue" : spesificationvalue,
            "notes_product" : request.POST.get('notes')
        }
        request.session['data'] = jsondata
        return redirect('cekjson', Product=value_product)
    return render(request, 'order/order.html', {'Product' : value_product})

def OrderNextView(request,Product):
    data = request.session.get('data')
    if data and data['product'] == Product and data["buyer"] == request.user.username:
        order = data
        extrak_product_data = product.objects.get(name_product = Product)
        address_data = Address.objects.get(user_id = request.user, id = data['address'])
        pre_order = None
        
        if request.method == "POST":
            checkout_model = Order(
                buyer_id   = request.user,
                store_id   = extrak_product_data.store_id,
                pre_order_time = None,
                address_buyer = address_data,
                quantity_order = data['quantity'],
                product = extrak_product_data,
                spesification = data['spesification'],
                spesificationvalue = data['spesificationvalue'],
                total_price = request.POST.get('total_price'),
                created_at = timezone.now()
            )
            checkout_model.save()
            return redirect('index')
    else:
        return redirect('orderproduct', Product = Product)        
        
    return render(request, 'order/ordernext.html', {"order" : order,'extrax_product_data' : extrak_product_data,"address_data" : address_data})


def detailorder(request,order_id):
    order = Order.objects.get(buyer_id = request.user, id = order_id)
    return render(request, 'order/detailorder.html', {"order" : order,} )

def orderflow(request,order_id):
    order = Order.objects.get(buyer_id = request.user, id = order_id)
    return render(request, 'order/orderflow.html',{"order":order,})

def storeorderflow(request,order_id):
    order = Order.objects.get(buyer_id = request.user, id = order_id)
    return render(request, 'order/storeorderflow.html',{"order":order,})