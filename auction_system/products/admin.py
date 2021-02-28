from django.contrib import admin
from django.contrib import admin

from .models import Product, AuctionedProduct

admin.site.register(Product)
admin.site.register(AuctionedProduct)
