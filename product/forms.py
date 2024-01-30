from django import forms
from .models import product
from multiupload.fields import MultiFileField
from django.core.validators import FileExtensionValidator

class ProductForm(forms.ModelForm):
    name_product = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    spesification = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}),  max_length=100)
    qty = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    price = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}), required=True, max_length=100)
    valuespesification = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control border"}),  max_length=200)
    category = forms.ChoiceField(widget=forms.Select(attrs={"class": "form-select border"}), choices=product.CATEGORY_CHOICES)
    image_product = MultiFileField(min_num=1, max_num=10, max_file_size=1024*1024*5, validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png'])])
    description = forms.Textarea( )
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['image_product'].widget.attrs.update({
            'class': 'form-control border ',
            'accept':'image/*',
            'style': 'padding: 6px 9px !important'

        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control border ',
            'style': 'resize: none;',
        })
        
    class Meta:
        model = product
        fields = ['name_product', 'description', 'category',  'price','qty']

