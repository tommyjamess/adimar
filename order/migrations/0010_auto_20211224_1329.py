# Generated by Django 3.2.7 on 2021-12-24 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_remove_loveit_user'),
        ('order', '0009_alter_order_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total',
            new_name='price',
        ),
        migrations.RemoveField(
            model_name='order',
            name='city',
        ),
        migrations.RemoveField(
            model_name='order',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='nearest_stop',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_one',
        ),
        migrations.RemoveField(
            model_name='order',
            name='phone_two',
        ),
        migrations.RemoveField(
            model_name='order',
            name='state',
        ),
        migrations.RemoveField(
            model_name='order',
            name='street',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='productordered', to='products.product'),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='city',
            field=models.CharField(choices=[('Ikeja', 'Ikeja'), ('Yaba', 'Yaba'), ('Oshodi', 'Oshodi'), ('Egbeda', 'Egbeda'), ('Surulere', 'Surulere'), ('Ikotun', 'Ikotun'), ('Ketu', 'Ketu'), ('Mile 12', 'Mile 12'), ('Mile 2', 'Mile 2'), ('Festac', 'Festac'), ('Okokomaiko', 'Okokomaiko'), ('Lekki', 'Lekki'), ('Ibeju Lekki', 'Ibeju Lekki'), ('Aja', 'Aja'), ('Ogba', 'Ogba'), ('Costain', 'Costain'), ('Ogudu', 'Ogudu'), ('Magodo Phase 1', 'Magodo Phase 1'), ('Magodo Phase 2', 'Magodo Phase 2'), ('Bariga', 'Bariga'), ('Victoria Island', 'Victoria Island'), ('Iyana Ipaja', 'Iyana Ipaja'), ('Agege', 'Agege'), ('Gbagada', 'Gbagada'), ('Omole', 'Omole'), ('Mushin', 'Mushin'), ('Abule Egba', 'Abule Egba'), ('Iyana Oworo', 'Iyana Oworo'), ('Bergar', 'Bergar'), ('Satellite Town', 'Satellite Town'), ('Sangotedo', 'Sangotedo'), ('Ebute Meta', 'Ebute Meta'), ('Ikota', 'Ikota'), ('Fagba', 'Fagba'), ('Pangroove', 'Pangroove'), ('Onipanu', 'Onipanu'), ('Outside Lagos', 'Outside Lagos'), ('Ikorodu', 'Ikorodu')], default='Ikeja', max_length=30),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='nearest_stop',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='phone_one',
            field=models.CharField(default=0, max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='phone_two',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='state',
            field=models.CharField(choices=[('Abia', 'Abia'), ('Adamawa', 'Akwa-ibom'), ('Edo', 'Edo'), ('Imo', 'Imo'), ('Lagos', 'Lagos'), ('Ondo', 'Ondo'), ('Abia', 'Abia'), ('Abia', 'Abia'), ('Abia', 'Abia')], default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='street',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='order_placed',
            field=models.BooleanField(default=False),
        ),
    ]