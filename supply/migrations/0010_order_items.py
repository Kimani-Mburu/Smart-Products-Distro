# Generated by Django 3.2.9 on 2021-11-27 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supply', '0009_alter_order_reference_no'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supply.product')),
            ],
        ),
    ]
