from django.contrib import admin
from django.contrib import admin

from .models import Product, AuctionedProduct, AccountProduct

admin.site.register(Product)
admin.site.register(AuctionedProduct)
admin.site.register(AccountProduct)
