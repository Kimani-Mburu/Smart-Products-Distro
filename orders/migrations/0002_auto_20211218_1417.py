# Generated by Django 3.2.9 on 2021-12-18 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_other_charge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('charges_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.othercharge')),
            ],
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='purchaseorder',
            name='other_Charges',
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_address',
            field=models.CharField(max_length=30, verbose_name='Delivery Address'),
        ),
        migrations.DeleteModel(
            name='OrderOtherCharge',
        ),
        migrations.DeleteModel(
            name='PurchaseOrder',
        ),
        migrations.AddField(
            model_name='order_other_charge',
            name='order_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
        ),
    ]
