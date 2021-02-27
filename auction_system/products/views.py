from django.shortcuts import render
from django.shortcuts import render, redirect
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


class ProductCreateView(LoginCreateView):
    template_name = 'products/product_create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products:all')



class ProductEditView(LoginUpdateView):
    template_name = 'products/product_edit.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('products:all')


class ProductDeleteView(LoginDeleteView):
    template_name_check_delete = 'products/product_confirm_delete.html'
    form_class = ProductForm
    queryset = Product.objects.all()
    success_url = reverse_lazy('products:all')
