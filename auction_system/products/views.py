from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from core.views import (
    LoginListView,
    LoginCreateView,
    LoginUpdateView,
    LoginDeleteView,
)

from .models import Product
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

        return HttpResponseRedirect(self.get_success_url())

class ProductDeleteView(LoginDeleteView):
    template_name_check_delete = 'products/product_confirm_delete.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('products:all')
