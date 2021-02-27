from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductEditView,
)

app_name = 'products'

urlpatterns = [
    path(
        'all/',
        ProductListView.as_view(),
        name='all',
    ),
    path(
        'create/',
        ProductCreateView.as_view(),
        name='create',
    ),
    path(
        '<int:pk>/',
        ProductEditView.as_view(),
        name="edit_detail",
    ),
    path(
        'delete/<int:pk>/',
        ProductDeleteView.as_view(),
        name="delete_product",
    ),
]
