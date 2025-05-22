from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'sku', 'category', 'image']

class ProductSoftDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []  # لا حاجة لأي حقول، فقط نعدل is_deleted داخل view

class ProductHardDeleteForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = []  # لا حاجة لأي حقول هنا أيضًا
