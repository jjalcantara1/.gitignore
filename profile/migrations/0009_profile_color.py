# Generated by Django 4.2.4 on 2023-10-10 13:56

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0008_remove_profile_color_profile_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='color',
            field=colorfield.fields.ColorField(default='#FFFFFF', image_field=None, max_length=25, samples=None),
        ),
    ]
