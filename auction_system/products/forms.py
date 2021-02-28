from django.forms import ModelForm, TextInput, NumberInput

from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'owner_supplier',
            'product_cost',
            'product_rarity'
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'start_date': TextInput(attrs={'class': 'form-control'}),
            'product_cost': NumberInput(attrs={'class': 'form-control'}),
            'product_rarity': TextInput(attrs={'class': 'form-control'}),

        }

