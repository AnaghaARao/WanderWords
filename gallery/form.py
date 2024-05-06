# Creating a form to edit a blog when user requests

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','image']