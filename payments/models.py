from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class DelFee(models.Model):
    loc1 = models.CharField(max_length=50)
    fee1 = models.CharField(max_length=50)
    loc2 = models.CharField(max_length=50)
    fee2 = models.CharField(max_length=50)
    loc3 = models.CharField(max_length=50)
    fee3 = models.CharField(max_length=50)
    loc4 = models.CharField(max_length=50)
    fee4 = models.CharField(max_length=50)
    loc5 = models.CharField(max_length=50)
    fee5 = models.CharField(max_length=50)
    loc6 = models.CharField(max_length=50)
    fee6 = models.CharField(max_length=50)
    loc7 = models.CharField(max_length=50)
    fee7 = models.CharField(max_length=50)
    loc8 = models.CharField(max_length=50)
    fee8 = models.CharField(max_length=50)
    loc9 = models.CharField(max_length=50)
    fee9 = models.CharField(max_length=50)
    loc10 = models.CharField(max_length=50)
    fee10 = models.CharField(max_length=50)
    loc11 = models.CharField(max_length=50)
    fee11 = models.CharField(max_length=50)
    loc12 = models.CharField(max_length=50)
    fee12 = models.CharField(max_length=50)
    loc13 = models.CharField(max_length=50)
    fee13 = models.CharField(max_length=50)
    loc14 = models.CharField(max_length=50)
    fee14 = models.CharField(max_length=50)
    loc15 = models.CharField(max_length=50)
    fee15 = models.CharField(max_length=50)
    loc16 = models.CharField(max_length=50)
    fee16 = models.CharField(max_length=50)
    loc17 = models.CharField(max_length=50)
    fee17 = models.CharField(max_length=50)
    loc18 = models.CharField(max_length=50)
    fee18 = models.CharField(max_length=50)
    loc19 = models.CharField(max_length=50)
    fee19 = models.CharField(max_length=50)
    loc20 = models.CharField(max_length=50)
    fee20 = models.CharField(max_length=50)
    loc21 = models.CharField(max_length=50, null=True)
    fee21 = models.CharField(max_length=50, null=True)
    loc22 = models.CharField(max_length=50,null=True)
    fee22 = models.CharField(max_length=50,null=True)
    loc23 = models.CharField(max_length=50,null=True)
    fee23 = models.CharField(max_length=50,null=True)
    loc24 = models.CharField(max_length=50,null=True)
    fee24 = models.CharField(max_length=50,null=True)
    loc25 = models.CharField(max_length=50,null=True)
    fee25 = models.CharField(max_length=50,null=True)
    loc26 = models.CharField(max_length=50,null=True)
    fee26 = models.CharField(max_length=50,null=True)
    loc27 = models.CharField(max_length=50,null=True)
    fee27 = models.CharField(max_length=50,null=True)
    loc28 = models.CharField(max_length=50,null=True)
    fee28 = models.CharField(max_length=50,null=True)
    loc29 = models.CharField(max_length=50,null=True)
    fee29 = models.CharField(max_length=50,null=True)
    loc30 = models.CharField(max_length=50,null=True)
    fee30 = models.CharField(max_length=50,null=True)
    loc31 = models.CharField(max_length=50,null=True)
    fee31 = models.CharField(max_length=50,null=True)
    loc32 = models.CharField(max_length=50,null=True)
    fee32 = models.CharField(max_length=50,null=True)
    loc33 = models.CharField(max_length=50,null=True)
    fee33 = models.CharField(max_length=50,null=True)
    loc34 = models.CharField(max_length=50,null=True)
    fee34 = models.CharField(max_length=50,null=True)
    loc35 = models.CharField(max_length=50,null=True)
    fee35 = models.CharField(max_length=50,null=True)
    loc36 = models.CharField(max_length=50,null=True)
    fee36 = models.CharField(max_length=50,null=True)
    loc37 = models.CharField(max_length=50,null=True)
    fee37 = models.CharField(max_length=50,null=True)
    loc38 = models.CharField(max_length=50,null=True)
    fee38 = models.CharField(max_length=50,null=True)
    

    def __str__(self):
        return self.loc1



class ShippingFee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(default=1500)
    city = models.CharField(max_length=50, default='Mushin')

    def __str__(self):
        return (self.user)

    class Meta:
        db_table = 'shippingfee'
        managed = True
        verbose_name = 'shippingfee'
        verbose_name_plural = 'shippingfee'