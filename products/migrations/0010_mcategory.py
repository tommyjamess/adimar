# Generated by Django 3.2.7 on 2021-09-27 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_rename_cat_list_category_clist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
