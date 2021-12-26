from django.contrib import admin
from user.models import BillingInfo


class AdminBillingInfo(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'street', 'nearest_stop', 'city', 'state', 'phone_one', 'phone_two', 'status', 'created_at', 'updated_at',)


admin.site.register(BillingInfo, AdminBillingInfo)
