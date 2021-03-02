from django.shortcuts import render
from django.utils import timezone
from django.http import Http404
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.base import RedirectView
from django.urls import reverse, reverse_lazy
from core.views import (
    LoginListView,
    LoginCreateView,
    LoginUpdateView,
    LoginGenericView,
    LoginDeleteView,
    LoginDetailView,
)

from .models import Product, AccountProduct
from auction.models import Auction
from .forms import ProductForm


class ProductListView(LoginListView):
    template_name = 'products/product_list.html'
    model = Product
    context_object_name = 'product_list'
    queryset = Product.objects.all()

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(
            created_by=user
        )


class ProductCreateView(LoginCreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:all')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        #  Needs a Seperate Save Method for Many to Many Relationships
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())


class ProductEditView(LoginUpdateView):
    template_name = 'products/product_edit.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('products:all')

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()

        #  Needs a Seperate Save Method for Many to Many Relationships
        form.save_m2m()

        return HttpResponseRedirect(self.get_success_url())

class ProductDeleteView(LoginDeleteView):
    template_name_check_delete = 'products/product_confirm_delete.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('products:all')


class BiddableProductAuctionListView(LoginListView):
    template_name = 'products/biddable_product_list.html'
    model = Product
    context_object_name = 'product_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        auction_id = self.kwargs.get('pk')

        context['auction'] = Auction.objects.get(
            id=auction_id,
        )

        return context

    def get_queryset(self, **kwargs):
        user = self.request.user
        auction_id = self.kwargs.get('pk')

        return Product.objects.filter(
            auction=auction_id,
        )


class BiddableAuctionProductDetailView(LoginDetailView):
    template_name = 'products/biddable_auction_product.html'
    model = Product
    context_object_name = 'auctioned_product'

    def get_context_data(self, **kwargs):
        auctioned_product = self.get_object()
        context = super().get_context_data(**kwargs)

        instance = AccountProduct.objects.filter(
            product=auctioned_product,
            account=self.request.user,
        )

        if instance:
            context['given_bid'] = instance.first().given_bid
        else:
            context['given_bid'] = 0

        return context

    def get_queryset(self, **kwargs):
        product_id = self.kwargs.get('pk')

        instance = Product.objects.filter(
            id=product_id,
        )

        return instance

    def post(self, request, **kwargs):
        auctioned_product = self.get_object()
        new_bid = request.POST.get('bid')
        auction = auctioned_product.auction

        instance = AccountProduct.objects.filter(
            product=auctioned_product,
            account=self.request.user,
        )

        if int(new_bid) > auction.highest_bid:
            auction.highest_bid = int(new_bid)
            auction.save()


        if int(new_bid) > auctioned_product.highest_bid:
            auctioned_product.highest_bid = int(new_bid)
            auctioned_product.save()

        if not new_bid:
            raise Http404('No New Paper')

        if not instance:
            AccountProduct.objects.create(
                product=auctioned_product,
                account=self.request.user,
                given_bid=new_bid,
            )
        else:
            AccountProduct.objects.filter(
                product=auctioned_product,
                account=self.request.user,
            ).update(given_bid=new_bid)

        return super().get(request, **kwargs)


class BiddedAccountProductListView(LoginListView):
    template_name = 'products/bidded_products_list.html'
    model = Product
    context_object_name = 'product_list'

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(
            bidders=user,
            is_claimed=False,
        )


class UnclaimedProductListView(LoginListView):
    template_name = 'products/unclaimed_products_list.html'
    model = Product
    context_object_name = 'product_list'

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(
            bidders=user,
            is_claimed=False,
            auction__end_date__lt=timezone.now(),
            is_released=True,
        )


class ClaimProductView(RedirectView):

    def get_redirect_url(self,**kwargs):
        product_id = kwargs.get('pk')

        Product.objects.filter(
            id=product_id,
        ).update(
            is_claimed=True,
        )

        return reverse('products:all_products_claimed')


class ClaimedProductListView(LoginListView):
    template_name = 'products/claimed_products_list.html'
    model = Product
    context_object_name = 'product_list'

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(
            bidders=user,
            is_claimed=True,
            winning_bidder=user,
            auction__end_date__lt=timezone.now(),
            is_released=True,
        )


class ReleasableProductListView(LoginListView):
    template_name = 'products/releasable_products_list.html'
    model = Product
    context_object_name = 'product_list'

    def get_queryset(self):
        user = self.request.user

        return Product.objects.filter(
            auction__created_by=user,
            auction__end_date__lt=timezone.now(),
            is_claimed=False,
            is_released=False,
        )


class ReleaseProductToWinnerView(LoginGenericView):
    template_name = 'products/release_to_winner.html'

    def post(self, request, **kwargs):
        product_id = kwargs.get('pk')
        product = Product.objects.get(id=product_id)

        winning_bidder = AccountProduct.objects.filter(
            product=product_id,
        ).order_by('given_bid')[0]

        if winning_bidder:
            if product.highest_bid == winning_bidder.given_bid:
                Product.objects.filter(
                    id=product_id,
                ).update(
                    is_released=True,
                    winning_bidder=winning_bidder.account
                )

        return redirect('products:all_products_releasable')
