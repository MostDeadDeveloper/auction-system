from django.urls import path

from .views import (
    AuctionListView,
    AuctionCreateView,
    AvailableAuctionListView,
    AuctionEditView,
    AuctionDeleteView,
    AuctionParticipantJoinView,
    OngoingAuctionListView,
)

app_name = 'auction'

urlpatterns = [
    path(
        'all/',
        AuctionListView.as_view(),
        name='all_auctions',
    ),
    path(
        'all/available/',
        AvailableAuctionListView.as_view(),
        name='all_auctions_available',
    ),
    path(
        'all/ongoing/',
        OngoingAuctionListView.as_view(),
        name='all_auctions_ongoing',
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
        '<int:pk>/join/',
        AuctionParticipantJoinView.as_view(),
        name="join_auction",
    ),
    path(
        'delete/<int:pk>/',
        AuctionDeleteView.as_view(),
        name="delete_auction",
    ),
]
