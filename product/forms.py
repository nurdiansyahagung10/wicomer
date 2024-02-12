from django import forms
from .models import product
from multiupload.fields import MultiFileField
from django.core.validators import FileExtensionValidator

class ProductForm(forms.ModelForm):
    name_product = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    spesification = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}),  max_length=100)
    quantity_product = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    price_product = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    valuespesification = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}),  max_length=200)
    category_product = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select border"}), choices=product.CATEGORY_CHOICES)
    kind = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select border"}), choices=product.KIND_CHOICHES)
    pre_order_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    description_product = forms.Textarea()
    image_product = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5, validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image_product'].widget.attrs.update({
            'class': 'form-control border ',
            'accept':'image/*',
            'style': 'padding: 6px 9px !important'

        })
        self.fields['description_product'].widget.attrs.update({
            'class': 'form-control border ',
            'style': 'resize: none;',
        })

    class Meta:
        model = product
        fields = ['image_product', 'description_product']
