from django.shortcuts import render
from django.views.generic.list import ListView
# Create your views here.

from .models import Auction

class AuctionListView(ListView):
    model = Auction
