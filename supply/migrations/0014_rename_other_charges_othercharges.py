# Generated by Django 3.2.9 on 2021-12-10 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0013_rename_order_other_charges_orderothercharges'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Other_Charges',
            new_name='OtherCharges',
        ),
    ]
