# Generated by Django 3.2.15 on 2022-10-17 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trades', '0012_auto_20221017_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trade',
            name='initial_share_value',
        ),
    ]