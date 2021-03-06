# Generated by Django 3.2.7 on 2021-09-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'brand',
                'verbose_name_plural': 'brands',
                'db_table': 'brand',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'db_table': 'category',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_range', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'price range',
                'verbose_name_plural': 'price ranges',
                'db_table': 'pricerange',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.PositiveIntegerField()),
                ('dis_price', models.PositiveIntegerField()),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('colors', models.CharField(max_length=1000)),
                ('sizes', models.CharField(max_length=1000)),
                ('availability', models.CharField(choices=[('In stock', 'In stock'), ('Out of stock', 'Out of stock')], max_length=20)),
                ('product_code', models.CharField(default='none', max_length=10000)),
                ('image', models.ImageField(upload_to='uploads/')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
                'db_table': 'product',
                'managed': True,
            },
        ),
    ]
