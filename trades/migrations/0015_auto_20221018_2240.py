# Generated by Django 3.2.15 on 2022-10-18 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0014_trade_initial_share_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='trade',
            name='latest_gain_loss',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='trade',
            name='latest_share_value',
            field=models.DecimalField(decimal_places=2, max_digits=15, null=True),
        ),
    ]
