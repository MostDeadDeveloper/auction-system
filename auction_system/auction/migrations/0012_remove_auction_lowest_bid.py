# Generated by Django 2.2.18 on 2021-03-02 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0011_remove_auction_auction_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='lowest_bid',
        ),
    ]