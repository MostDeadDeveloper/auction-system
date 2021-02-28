# Generated by Django 2.2.18 on 2021-02-27 21:15

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auction', '0005_auto_20210227_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='particating_members',
            field=models.ManyToManyField(through='auction.AuctionParticipant', to=settings.AUTH_USER_MODEL),
        ),
    ]