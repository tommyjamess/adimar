# Generated by Django 3.2.7 on 2021-12-28 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_remove_loveit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='bulk_price',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='dis_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
