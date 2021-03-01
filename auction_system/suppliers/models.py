from django.db import models
from django.conf import settings

from core.models import BaseModel

class Supplier(BaseModel):
    name = models.CharField(max_length=64)
    preferred_name = models.CharField(max_length=50)
    particating_members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        name='members',
    )
    #  auctions
    main_account = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.CASCADE,
        related_name='main_supplier'
    )

    def __str__(self):
        return self.name
