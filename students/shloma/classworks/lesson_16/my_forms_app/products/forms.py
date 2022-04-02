from django import forms
from django.core.validators import MinValueValidator
from .models import Products


class ProductsForm(forms.Form):
    name = forms.CharField(label="Product name")

    supplier = forms.CharField(label="Supplier")

    current_amont = forms.IntegerField(label="Amount",
                                       validators=[MinValueValidator(0)])


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ["current_amont"]
        # fields = ["name", "supplier", "current_amont"]
