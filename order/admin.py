from django.contrib import admin
from . models import Cart, Order, OrderPlaced


class AdminCart(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'color', 'size', 'order_code', 'order_placed')

class AdminOrder(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'color', 'size', 'price', 'order_placed', 'payment_code', 'status', 'created_at', 'updated_at',)

class AdminOrderPlaced(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'street', 'nearest_stop', 'city', 'state', 'phone_one', 'phone_two',  'total', 'order_placed', 'order_code', 'payment_code', 'payment_verified', 'status', 'created_at', 'updated_at')



admin.site.register(Cart, AdminCart)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderPlaced, AdminOrderPlaced)

