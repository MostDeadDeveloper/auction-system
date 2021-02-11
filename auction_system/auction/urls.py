from django.urls import path

from .views import AuctionListView

app_name = 'auction'

urlpatterns = [
    path(
        'all/',
        AuctionListView.as_view(),
        name='all_auctions',
    )
]
