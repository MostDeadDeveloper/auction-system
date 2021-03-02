from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.views import LoginView

from core.views import LoginGenericView, GenericView

class BaseRedirectView(RedirectView):

    def get_redirect_url(self, **kwargs):
        user = self.request.user

        if not user.is_authenticated:
            return reverse('account:account_login')

        return reverse('account:dashboard')


class DashboardView(LoginGenericView):
    template_name = 'account/index.html'


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

