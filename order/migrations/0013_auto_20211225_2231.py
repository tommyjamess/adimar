# Generated by Django 3.2.7 on 2021-12-25 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0012_auto_20211225_1513'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'managed': True, 'verbose_name': 'order', 'verbose_name_plural': 'order'},
        ),
        migrations.AlterModelOptions(
            name='orderplaced',
            options={'managed': True, 'verbose_name': 'orderplaced', 'verbose_name_plural': 'orderplaced'},
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.AlterModelTable(
            name='orderplaced',
            table='orderplaced',
        ),
    ]
