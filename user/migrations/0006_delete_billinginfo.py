# Generated by Django 3.2.7 on 2021-10-11 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_billinginfo_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BillingInfo',
        ),
    ]
