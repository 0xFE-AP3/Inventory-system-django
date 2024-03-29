# Generated by Django 4.1 on 2022-09-07 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_order_options_remove_product_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Scaricati'},
        ),
        migrations.AlterField(
            model_name='order',
            name='order_quantity',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('trans_id', models.AutoField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('time', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.product')),
            ],
        ),
    ]
