# Generated by Django 2.2.18 on 2021-03-01 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_auctionparticipant_given_bid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionparticipant',
            name='given_bid',
        ),
    ]
