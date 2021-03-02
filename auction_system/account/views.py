from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.views import LoginView

from core.views import LoginGenericView, GenericView, LoginListView

from auction.models import Auction

class BaseRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return reverse('account:account_login')

        if user.is_bidder:
            return reverse('products:all_products_bidded')
        else:
            return reverse('account:supplier_dashboard')


class SupplierDashboardView(LoginListView):
    template_name = 'account/supplier_index.html'
    model = Auction

    def get_queryset(self, **kwargs):
        user = self.request.user
        return Auction.objects.filter(
            created_by=user,
            is_active=True,
            start_date__lt=timezone.now(),
            end_date__gt=timezone.now(),
        )


class CustomLoginView(LoginView):
    template_name = 'account/login.html'

    def post(self, request):
        user = self.request.user
        username = request.session.get('Email')
        password = request.session.get('pass')

        authenticate(
            username=username,
            password=password,
        )

        if not user.is_authenticated:
            return reverse('account:account_login')

        return reverse('account:dashboard')

