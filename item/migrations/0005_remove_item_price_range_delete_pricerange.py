# Generated by Django 4.2.4 on 2023-10-13 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_pricerange_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='price_range',
        ),
        migrations.DeleteModel(
            name='PriceRange',
        ),
    ]