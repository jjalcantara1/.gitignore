# Generated by Django 4.2.4 on 2023-10-10 14:18

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0010_alter_profile_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None),
        ),
    ]
