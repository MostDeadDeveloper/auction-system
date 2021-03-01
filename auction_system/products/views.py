from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from core.views import (
    LoginListView,
    LoginCreateView,
    LoginUpdateView,
    LoginDeleteView,
    LoginDetailView,
)

from .models import Product, AuctionedProduct, AccountProduct
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
            created_by=user,
            auctionedproduct__auction=auction_id,
        )


class BiddableAuctionProductDetailView(LoginDetailView):
    template_name = 'products/biddable_auction_product.html'
    model = AuctionedProduct
    context_object_name = 'auctioned_product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context

    def get_queryset(self, **kwargs):
        product_id = self.kwargs.get('pk')
        auction_id = self.kwargs.get('auction_id')

        instance = AuctionedProduct.objects.filter(
            product=product_id,
            auction=auction_id
        )

        return instance

    def post(self, request, **kwargs):
        auctioned_product = self.get_object()
        product = auctioned_product.product
        new_bid = request.POST.get('bid')

        instance = AccountProduct.objects.filter(
            product=product,
            account=self.request.user,
        )

        if not instance:
            AccountProduct.objects.create(
                product=product,
                account=self.request.user,
                given_bid=new_bid,
            )
        else:
            AccountProduct.objects.filter(
                product=product,
                account=self.request.user,
            ).update(given_bid=new_bid)

        return super().get(request, **kwargs)
