# Generated by Django 3.2.15 on 2022-10-17 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0009_alter_trade_company_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='latest_gain_loss',
        ),
    ]
