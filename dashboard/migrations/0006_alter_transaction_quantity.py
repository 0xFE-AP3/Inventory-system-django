# Generated by Django 4.1 on 2022-09-07 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_order_options_alter_order_order_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
