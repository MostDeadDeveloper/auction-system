from django.forms import (
    ModelForm,
    TextInput,
    NumberInput,
    SelectMultiple,
)

from .models import Auction

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        fields = [
            'name',
            'start_date',
            'end_date',
            'minimum_bid_requirement',
        ]
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'start_date': TextInput(attrs={'class': 'form-control'}),
            'end_date': TextInput(attrs={'class': 'form-control'}),
            'highest_bid': NumberInput(attrs={'class': 'form-control'}),
            'lowest_bid': NumberInput(attrs={'class': 'form-control'}),
            'products': SelectMultiple(attrs={'class': 'form-control'}),
            'minimum_bid_requirement': NumberInput(attrs={'class': 'form-control'}),
        }
