from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from core.views import (
    LoginListView,
    LoginCreateView,
    LoginUpdateView,
    LoginDeleteView,
)

from .models import Auction
from .forms import AuctionForm

class AuctionListView(LoginListView):
    template_name = 'auction/auction_list.html'
    model = Auction
    context_object_name = 'auction_list'
    queryset = Auction.objects.all()


class AuctionCreateView(LoginCreateView):
    template_name = 'auction/auction_create.html'
    form_class = AuctionForm


class AuctionEditView(LoginUpdateView):
    template_name = 'auction/auction_edit.html'
    form_class = AuctionForm
    queryset = Auction.objects.all()
    success_url = reverse_lazy('auction:all_auctions')


class AuctionDeleteView(LoginDeleteView):
    form_class = AuctionForm
    success_url = reverse_lazy('auction:all_auctions')
    queryset = Auction.objects.all()
