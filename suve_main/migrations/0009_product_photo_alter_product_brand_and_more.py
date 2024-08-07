# Generated by Django 5.0.7 on 2024-07-26 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suve_main', '0008_alter_routes_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=255, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=255, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Product_name'),
        ),
    ]
