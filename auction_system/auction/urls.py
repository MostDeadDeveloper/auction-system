from django.urls import path

from .views import (
    AuctionListView,
    AuctionCreateView,
    AuctionEditView,
    AuctionDeleteView,
)

app_name = 'auction'

urlpatterns = [
    path(
        'all/',
        AuctionListView.as_view(),
        name='all_auctions',
    ),
    path(
        'create/',
        AuctionCreateView.as_view(),
        name='create',
    ),
    path(
        '<int:pk>/',
        AuctionEditView.as_view(),
        name="edit_detail",
    ),
    path(
        'delete/<int:pk>/',
        AuctionDeleteView.as_view(),
        name="delete_auction",
    ),
]
