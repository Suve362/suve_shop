from django import forms
from .models import ProductPhoto


class ProductForm(forms.Form):
    photo = forms.ImageField()

    class Meta:
        model = ProductPhoto
        fields = ['photo']
