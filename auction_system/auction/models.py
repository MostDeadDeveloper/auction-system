from django.db import models
from django.conf import settings
from django.utils import timezone
from core.models import BaseModel


class Auction(BaseModel):
    name = models.CharField(max_length=128)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(null=True)
    particating_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through='auction.AuctionParticipant',
        through_fields=('auction','account'),
    )
    highest_bid = models.IntegerField(default=0)
    minimum_bid_requirement = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class AuctionParticipant(BaseModel):
    auction = models.ForeignKey(
        'auction.Auction',
        null=True,
        on_delete=models.CASCADE,
    )
    account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
    )
