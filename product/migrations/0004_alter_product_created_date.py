# Generated by Django 4.1.1 on 2022-09-22 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_cart_product_alter_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2022, 9, 22, 18, 2, 21, 308003)),
        ),
    ]
