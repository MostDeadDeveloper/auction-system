from django.db import models

from core.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=64)
    owner_supplier = models.ForeignKey(
        'suppliers.Supplier',
        null=True,
        on_delete=models.CASCADE,
        related_name='owner_supplier',
    )
    product_cost = models.IntegerField(default=0)
    product_rarity = models.CharField(max_length=128)


class AuctionedProduct(BaseModel):
    auction = models.ForeignKey(
        'auction.Auction',
        null=True,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        'products.Product',
        null=True,
        on_delete=models.CASCADE,
    )
