from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    clist = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cat_name

    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class PriceRange(models.Model):
    price_range = models.CharField(max_length=20)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.price_range 
    
    class Meta:
        db_table = 'pricerange'
        managed = True
        verbose_name = 'price range'
        verbose_name_plural = 'price ranges'

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brand_name 
    
    class Meta:
        db_table = 'brand'
        managed = True
        verbose_name = 'brand'
        verbose_name_plural = 'brands'
    
class Mcategory(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.name
    

class Product(models.Model):

    AVAILABILITY = (
        ("In stock", "In stock"),
        ("Out of stock", "Out of stock"),
    )

    TYPE = (
        ("main", "main"),
        ("custom", "custom"),
    )

    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=1)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING, default=3)
    prange = models.ForeignKey(PriceRange, on_delete=models.DO_NOTHING, default=2)
    mcat = models.ForeignKey(Mcategory, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225)
    price = models.PositiveIntegerField()
    bulk_price = models.PositiveIntegerField(default=0)
    dis_price = models.PositiveIntegerField()
    amount = models.IntegerField(blank=True, null=True)
    colors = models.CharField(max_length=1000)
    color_one = models.CharField(max_length=30, null=True, blank=True)
    color_two = models.CharField(max_length=30, null=True, blank=True)
    color_three = models.CharField(max_length=30, null=True, blank=True)
    color_four = models.CharField(max_length=30, null=True, blank=True)
    color_five = models.CharField(max_length=30, null=True, blank=True)
    color_six = models.CharField(max_length=30, null=True, blank=True)
    color_seven = models.CharField(max_length=30, null=True, blank=True)
    color_eight = models.CharField(max_length=30, null=True, blank=True)
    color_nine = models.CharField(max_length=30, null=True, blank=True)
    color_ten = models.CharField(max_length=30, null=True, blank=True)
    sizes = models.CharField(max_length=1000)
    availability = models.CharField(max_length=20, choices=AVAILABILITY)
    product_code = models.CharField(max_length=10000, default='none')
    image = models.ImageField(upload_to='images/')
    image_one = models.ImageField(upload_to='images/', blank=True, null=True)
    image_two = models.ImageField(upload_to='images/', blank=True, null=True)
    image_three = models.ImageField(upload_to='images/', blank=True, null=True)
    image_four = models.ImageField(upload_to='images/', blank=True, null=True)
    image_five = models.ImageField(upload_to='images/', blank=True, null=True)
    image_six = models.ImageField(upload_to='images/', blank=True, null=True)
    image_seven = models.ImageField(upload_to='images/', blank=True, null=True)
    image_eight = models.ImageField(upload_to='images/', blank=True, null=True)
    image_nine = models.ImageField(upload_to='images/', blank=True, null=True)
    image_ten = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    banner = models.BooleanField(default=False)
    adire = models.BooleanField(default=False)
    urban_wear = models.BooleanField(default=False)
    bags = models.BooleanField(default=False)
    gallery = models.BooleanField(default=False)
    order = models.CharField(max_length=6, default='main', choices=TYPE)

    def __str__(self):
        return str(self.name)

    
    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'product'
        verbose_name_plural = 'product'
    

class Customimg(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='images/')

    def __str__(self):
        return str(self.name)


class Loveit(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    value = models.CharField(max_length=6)

    def __str__(self):
        return str(self.product)
