from django.db import models

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=20)
    logo = models.ImageField(upload_to='uploads/')
    phone_one = models.CharField(max_length=14)
    phone_two = models.CharField(max_length=14)
    location = models.CharField(max_length=200)
    insta = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    bannerimg = models.ImageField(upload_to='uploads/', blank=True, null=True)

    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name_plural = 'setting'

