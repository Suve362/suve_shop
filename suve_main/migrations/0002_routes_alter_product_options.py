# Generated by Django 5.0.7 on 2024-07-19 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suve_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-brand']},
        ),
    ]
