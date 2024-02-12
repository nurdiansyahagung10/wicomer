from django.shortcuts import render,redirect, get_object_or_404
from .forms import ProductForm
from django.http import HttpResponse
from .models import product, ProductImage, ProductSpesification,SpesificationValue
from accounts.models import Store
# Create your views here.
def createproduct(request):
    form = ProductForm() 
    if request.method == 'POST':  
        store = get_object_or_404(Store, seller_id = request.user)
        name_product = request.POST.get('name_product') 
        description_product = request.POST.get('description_product')
        category_product = request.POST.get('category_product')
        price_product = request.POST.get('price_product')
        quantity_product = request.POST.get('quantity_product')
        kind = request.POST.get('kind')
        pre_order_date = request.POST.get('pre_order_date')
        Product = product(
            store_id = store,
            name_product = name_product, 
            description_product = description_product,
            category_product = category_product,
            price_product = price_product,
            quantity_product = quantity_product,
            kind = kind,
            pre_order_date = pre_order_date
        )
        Product.save()
        for uploaded_file in request.FILES.getlist('image_product'):
            product_image = ProductImage(product_id=Product, name_image=uploaded_file)
            product_image.save()
            
        for spesification in request.POST.getlist('spesification'):
            spesification_product = ProductSpesification(product_id=Product, name_Spesification = spesification)
            spesification_product.save()
        list = 0
        for valuespesification in request.POST.getlist('valuespesification'):
            Spesification = request.POST.getlist('spesification')
            spesification_name = ProductSpesification.objects.get(name_Spesification = Spesification[list],product_id = product.objects.get(name_product = name_product))
            valuespesification = SpesificationValue(spesification_id = spesification_name, name_value = valuespesification)
            valuespesification.save()
            list += 1

        return redirect('dashboardstore')
    return render(request, 'product/create_product.html', {'form' : form})
