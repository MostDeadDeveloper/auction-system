from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic.base import RedirectView
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy

from core.views import (
    LoginListView,
    LoginCreateView,
    LoginGenericView,
    LoginUpdateView,
    LoginDeleteView,
)

from .models import Auction, AuctionParticipant
from .forms import AuctionForm

class AuctionListView(LoginListView):
    template_name = 'auction/auction_list.html'
    model = Auction
    context_object_name = 'auction_list'

    def get_queryset(self):
        user = self.request.user

        return Auction.objects.filter(
            created_by=user
        )


class AuctionCreateView(LoginCreateView):
    template_name = 'auction/auction_create.html'
    form_class = AuctionForm
    success_url = reverse_lazy('auction:all_auctions')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        #  Needs a Seperate Save Method for Many to Many Relationships
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())


class AuctionEditView(LoginUpdateView):
    template_name = 'auction/auction_edit.html'
    form_class = AuctionForm
    queryset = Auction.objects.all()
    success_url = reverse_lazy('auction:all_auctions')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        #  Needs a Seperate Save Method for Many to Many Relationships
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())

class AuctionDeleteView(LoginDeleteView):
    form_class = AuctionForm
    success_url = reverse_lazy('auction:all_auctions')
    queryset = Auction.objects.all()


class AvailableAuctionListView(LoginListView):
    template_name = 'auction/auction_available_list.html'
    model = Auction
    context_object_name = 'auction_list'

    def get_queryset(self):
        user = self.request.user

        return Auction.objects.filter(
            is_active=True,
            start_date__gt=timezone.now(),
        ).exclude(particating_members=user)


class AuctionParticipantJoinView(RedirectView):

    def get_redirect_url(self,**kwargs):
        auction_id = kwargs.get('pk')

        AuctionParticipant.objects.create(
            auction_id=auction_id,
            account=self.request.user,
        )

        return reverse('auction:all_auctions_available')


class OngoingAuctionListView(LoginListView):
    template_name = 'auction/ongoing_auctions_list.html'
    model = Auction
    context_object_name = 'auction_list'

    def get_queryset(self):
        user = self.request.user

        return Auction.objects.filter(
            is_active=True,
            particating_members=user,
            start_date__gt=timezone.now(),
            end_date__lt=timezone.now(),
        )
