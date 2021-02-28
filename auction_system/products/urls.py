from django.urls import path

from .views import (
    ProductListView,
    ProductCreateView,
    ProductDeleteView,
    ProductEditView,
    BiddableProductAuctionListView,
    BiddableAuctionProductDetailView,
)

app_name = 'products'

urlpatterns = [
    path(
        'all/',
        ProductListView.as_view(),
        name='all',
    ),
    path(
        'all/auction/<int:pk>/biddable/',
        BiddableProductAuctionListView.as_view(),
        name='all_biddable',
    ),
    path(
        '<int:pk>/auction/<int:auction_id>/biddable/',
        BiddableAuctionProductDetailView.as_view(),
        name='auctioned_product_detail',
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
