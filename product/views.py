from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm
from django.http import HttpResponse
from .models import product, ProductImage, SpesificationProduct,SpesificationValue
from accounts.models import Store
# Create your views here.
def createproduct(request):
    form = ProductForm() 
    if request.method == 'POST':  
        store = get_object_or_404(Store, store_seller_id = request.user)
        name_product = request.POST.get('name_product') 
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        Product = product(
            store_id = store,
            name_product = name_product, 
            description = description,
            category = category,
            price = price,
            qty = qty
        )
        Product.save()
        for uploaded_file in request.FILES.getlist('image_product'):
            product_image = ProductImage(product=Product, image=uploaded_file)
            product_image.save()
            
        for spesification in request.POST.getlist('spesification'):
            spesification_product = SpesificationProduct(product=Product, name_Spesification = spesification)
            spesification_product.save()
        list = 0
        for valuespesification in request.POST.getlist('valuespesification'):
            Spesification = request.POST.getlist('spesification')
            spesification_name = SpesificationProduct.objects.get(name_Spesification = Spesification[list],product = product.objects.get(name_product = name_product))
            valuespesification = SpesificationValue(spesification= spesification_name, value_Spesification = valuespesification)
            valuespesification.save()
            list += 1

        return redirect('dashboardstore')
    return render(request, 'product/create_product.html', {'form' : form})
