from django.contrib import admin

from .models import Auction, AuctionParticipant

admin.site.register(Auction)
admin.site.register(AuctionParticipant)
