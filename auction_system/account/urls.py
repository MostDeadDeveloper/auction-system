from django.urls import path
from django.contrib.auth import views as auth_views

from .views import DashboardView, CustomLoginView

app_name = 'account'

urlpatterns = [
    path(
        'dashboard/',
        DashboardView.as_view(),
        name='dashboard',
    ),
    path(
        'user/login/',
        auth_views.LoginView.as_view(),
        {'template_name': 'account/login.html'},
        name='account_login',
    ),
]
