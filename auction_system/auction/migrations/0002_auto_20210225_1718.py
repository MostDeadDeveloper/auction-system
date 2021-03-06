# Generated by Django 2.2.18 on 2021-02-25 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='auction_type',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='auction',
            name='highest_bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auction',
            name='lowest_bid',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auction',
            name='minimum_bid_requirement',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='auction',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
