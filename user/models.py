from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BillingInfo(models.Model):

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null= True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    nearest_stop = models.CharField(max_length=50)
    city = models.CharField(max_length=30, choices= CITY)
    state = models.CharField(max_length=30, choices=STATES)
    phone_one = models.CharField(max_length=14)
    phone_two = models.CharField(max_length=14, null=True, blank=True)
    status = models.CharField(max_length=30, default='New')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.user)
    
    
    @property
    def username(self):
        if self.user_id is not None:
            return self.user.first_name + '' + '[' + self.user.username + '] '
    
    @property
    def email(self):
        if self.user_id is not None:
            return (self.user.email)

    class Meta:
        db_table = 'billinginfo'
        managed = True
        verbose_name = 'billinginfo'
        verbose_name_plural = 'billinginfo'