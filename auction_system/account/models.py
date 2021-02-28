from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import AccountManager

from core.models import BaseModel

class Account(AbstractUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    USERNAME_FIELD = 'email'
    username = models.CharField(
        max_length=24,
        unique=False,
        blank=True,
    )
    is_bidder = models.BooleanField(default=True)

    REQUIRED_FIELDS = []

    objects = AccountManager()

    def __str__(self):
        return self.email
