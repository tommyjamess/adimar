from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


from products.models import Product

# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    color = models.CharField(max_length=200, null=True)
    size = models.TextField()
    order_code = models.CharField(max_length=200, unique=True, editable=False)
    order_placed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.id}'
    
    @property
    def price(self):
        if self.product_id is not None:
            return (self.product.price)

    @property
    def amount(self):
        if self.product.id is None:
            return None
        else:
            if self.product.dis_price:
                return(self.product.dis_price * self.quantity)
            else:
                return(self.product.price * self.quantity)

    
    class Meta:
        db_table = 'cart'
        managed = True
        verbose_name = 'cart'
        verbose_name_plural = 'cart'

class Order(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Preparing', 'Preparing'),
        ('Onshipping', 'Onshipping'),
        ('Delivered', 'Delivered'),

    )

    

    

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='productordered')
    quantity = models.SmallIntegerField(default=0)
    color = models.CharField(max_length=150, default="displayed color")
    size = models.TextField(default="displayed size")
    price = models.FloatField(null=True, blank=True)
    order_placed = models.BooleanField(default=False)
    order_code = models.CharField(max_length=70, editable=True, null=True, blank=True)
    payment_code = models.CharField(max_length=8, editable=True)
    status = models.CharField(max_length=30, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return  str(self.user)
    

    class Meta:
        db_table = 'order'
        managed = True
        verbose_name = 'order'
        verbose_name_plural = 'order'


class OrderPlaced(models.Model):

    STATUS = (
        ('New', 'New'),
        ('Preparing', 'Preparing'),
        ('Onshipping', 'Onshipping'),
        ('Delivered', 'Delivered'),

    )

    STATES = (
    ('Abia', 'Abia'),
    ('Adamawa', 'Akwa-ibom'),
    ('Edo', 'Edo'),
    ('Imo', 'Imo'),
    ('Lagos', 'Lagos'),
    ('Ondo', 'Ondo'),
    ('Abia', 'Abia'),
    ('Abia', 'Abia'),
    ('Abia', 'Abia'),
    )

    CITY = (
        ('Ikeja', 'Ikeja'),
        ('Yaba', 'Yaba'),
        ('Oshodi', 'Oshodi'),
        ('Egbeda', 'Egbeda'),
        ('Surulere', 'Surulere'),
        ('Ikotun', 'Ikotun'),
        ('Ketu', 'Ketu'),
        ('Mile 12', 'Mile 12'),
        ('Mile 2', 'Mile 2'),
        ('Festac', 'Festac'),
        ('Okokomaiko', 'Okokomaiko'),
        ('Lekki', 'Lekki'),
        ('Ibeju Lekki', 'Ibeju Lekki'),
        ('Aja', 'Aja'),
        ('Ogba', 'Ogba'),
        ('Costain', 'Costain'),
        ('Ogudu', 'Ogudu'),
        ('Magodo Phase 1', 'Magodo Phase 1'),
        ('Magodo Phase 2', 'Magodo Phase 2'),
        ('Bariga', 'Bariga'),
        ('Victoria Island', 'Victoria Island'),
        ('Iyana Ipaja', 'Iyana Ipaja'),
        ('Agege', 'Agege'),
        ('Gbagada', 'Gbagada'),
        ('Omole', 'Omole'),
        ('Mushin', 'Mushin'),
        ('Abule Egba', 'Abule Egba'),
        ('Iyana Oworo', 'Iyana Oworo'),
        ('Bergar', 'Bergar'),
        ('Satellite Town', 'Satellite Town'),
        ('Sangotedo', 'Sangotedo'),
        ('Ebute Meta', 'Ebute Meta'),
        ('Ikota', 'Ikota'),
        ('Fagba', 'Fagba'),
        ('Pangroove', 'Pangroove'),
        ('Onipanu', 'Onipanu'),
        ('Outside Lagos', 'Outside Lagos'),
        ('Ikorodu', 'Ikorodu'),
    )


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    street = models.CharField(max_length=200, null=True)
    nearest_stop = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, choices= CITY, default='Ikeja')
    state = models.CharField(max_length=250, choices=STATES)
    phone_one = models.CharField(max_length=14)
    phone_two = models.CharField(max_length=14, null=True, blank=True)
    total = models.FloatField(null=True, blank=True)
    order_placed = models.BooleanField(default=False)
    order_code = models.CharField(max_length=200, editable=False, null=True, blank=True)
    payment_code = models.CharField(max_length=10, editable=False)
    payment_verified = models.BooleanField(default=False)
    status = models.CharField(max_length=40, choices=STATUS, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)
    

    class Meta:
        db_table = 'orderplaced'
        managed = True
        verbose_name = 'orderplaced'
        verbose_name_plural = 'orderplaced'

    