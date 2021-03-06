# Generated by Django 3.2.7 on 2021-10-11 17:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0006_delete_billinginfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('nearest_stop', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Akwa-ibom'), ('Edo', 'Edo'), ('Imo', 'Imo'), ('Lagos', 'Lagos'), ('Ondo', 'Ondo'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia')], max_length=30)),
                ('phone_one', models.CharField(max_length=14)),
                ('phone_two', models.CharField(blank=True, max_length=14, null=True)),
                ('status', models.CharField(default='New', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
