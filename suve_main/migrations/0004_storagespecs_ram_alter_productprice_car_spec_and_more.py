# Generated by Django 5.0.7 on 2024-07-22 20:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suve_main', '0003_rename_storage_storagespecs_rom_storagespecs_cpu'),
    ]

    operations = [
        migrations.AddField(
            model_name='storagespecs',
            name='ram',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='car_spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suve_main.carspecs'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='storage_spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suve_main.storagespecs'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='watch_spec',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='suve_main.watchspecs'),
        ),
        migrations.AlterField(
            model_name='storagespecs',
            name='cpu',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='watchspecs',
            name='connectivity',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
