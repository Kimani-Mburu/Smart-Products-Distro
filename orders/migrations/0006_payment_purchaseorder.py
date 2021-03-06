# Generated by Django 3.2.9 on 2021-12-23 17:10

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_rename_order_farmer_id_order_order_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchase_order_date', models.DateField(default=datetime.date.today)),
                ('purchase_order_total_value', models.FloatField()),
                ('purchase_order_status', models.CharField(choices=[('Shipped', 'Shipped'), ('Canceled', 'Canceled'), ('On-route', 'On-route'), ('Delivered', 'Delivered')], max_length=10)),
                ('purchase_order_Order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('purchase_order_Other_charges', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order_other_charge')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('M-pesa', 'M-pesa'), ('Cash', 'Cash')], max_length=10)),
                ('payment_total_price', models.FloatField()),
                ('payment_ref', models.CharField(blank=True, max_length=10, null=True)),
                ('payment_order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
