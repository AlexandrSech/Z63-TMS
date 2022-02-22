from django import forms


class ProductsForm(forms.Form):
    id = forms.IntegerField()
    current_amount = forms.CharField(label='Your current_amount', max_length=100)
