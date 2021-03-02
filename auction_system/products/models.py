from django.db import models
from django.conf import settings

from core.models import BaseModel

class Product(BaseModel):
    name = models.CharField(max_length=64)
    owner_supplier = models.ForeignKey(
        'suppliers.Supplier',
        null=True,
        on_delete=models.CASCADE,
        related_name='owner_supplier',
    )
    winning_bidder = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name='winning_bidder',
    )
    product_cost = models.IntegerField(default=0)
    auction = models.ForeignKey(
        'auction.Auction',
        null=True,
        on_delete=models.CASCADE,
        related_name='auctioned_product',
    )
    highest_bid = models.IntegerField(default=0)
    product_rarity = models.CharField(max_length=128)
    bidders = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='products.AccountProduct',
        through_fields=('product','account'),
    )
    is_claimed = models.BooleanField(default=False)
    is_released = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(
            self.name,
        )


class AccountProduct(BaseModel):
    account = models.ForeignKey(
        'account.Account',
        null=True,
        on_delete=models.CASCADE,
    )
    product = models.ForeignKey(
        'products.Product',
        null=True,
        on_delete=models.CASCADE,
    )
    given_bid = models.IntegerField(default=0, null=True)

    def __str__(self):
        return '{} - {}'.format(
            self.account.username,
            self.product.name,
        )
