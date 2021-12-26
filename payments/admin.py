from django.contrib import admin
from .models import DelFee, ShippingFee


class AdminDelFee(admin.ModelAdmin):
    list_display = ('loc1', 'fee1', 'loc2', 'fee2', 'loc3', 'fee3', 'loc4', 'fee4', 'loc5', 'fee5', 'loc6', 'fee6', 'loc7', 'fee7', 'loc8', 'fee8', 'loc9', 'fee9', 'loc10', 'fee11', 'loc12', 'fee12', 'loc13', 'fee13', 'loc14', 'fee14', 'loc15', 'fee15', 'loc16', 'fee16', 'loc17', 'fee17', 'loc18', 'fee18', 'loc19', 'fee19', 'loc20', 'fee20',)


class AdminShippingFee(admin.ModelAdmin):
    list_display = ('user', 'price', 'city')

admin.site.register(DelFee, AdminDelFee)
admin.site.register(ShippingFee, AdminShippingFee)