from django.contrib import admin
from . models import Setting

admin.site.site_header = "ADIMAR"

# Register your models here.

class SettingAdmin(admin.ModelAdmin):
    list_display = ('title', 'logo', 'phone_one', 'phone_two', 'location', 'bannerimg',)


admin.site.register(Setting, SettingAdmin)
