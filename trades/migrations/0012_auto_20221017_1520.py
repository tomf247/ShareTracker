# Generated by Django 3.2.15 on 2022-10-17 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0011_trade_latest_gain_loss'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='latest_gain_loss',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='latest_share_price',
        ),
        migrations.RemoveField(
            model_name='trade',
            name='latest_share_value',
        ),
    ]
