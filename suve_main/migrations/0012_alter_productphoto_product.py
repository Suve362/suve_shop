# Generated by Django 5.0.7 on 2024-07-26 19:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suve_main', '0011_remove_product_photo_productphoto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suve_main.product'),
        ),
    ]
