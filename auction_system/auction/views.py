from django.shortcuts import render
from core.views import LoginListView
# Create your views here.

from .models import Auction

class AuctionListView(LoginListView):
    template_name = 'auction/index.html'
    model = Auction
