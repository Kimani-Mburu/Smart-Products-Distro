# Generated by Django 3.2.9 on 2021-12-18 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_farmer'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Units',
            new_name='Unit',
        ),
    ]
