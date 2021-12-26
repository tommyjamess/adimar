from django.contrib import admin
from . models import Category, PriceRange, Brand, Product, Mcategory, Customimg, Loveit

# Register your models here.
class AdminCategory(admin.ModelAdmin):
    list_display = ('cat_name', 'image', 'clist', 'updated_at',)


class AdminPriceRange(admin.ModelAdmin):
    list_display = ('price_range', 'updated_at',)

class AdminBrand(admin.ModelAdmin):
    list_display = ('brand_name', 'updated_at',)


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'prange', 'mcat', 'order', 'price', 'bulk_price', 'dis_price', 'amount', 'colors', 'color_one', 'color_two', 'color_three', 'color_four', 'color_five', 'color_six', 'color_seven', 'color_eight', 'color_nine', 'color_ten', 'sizes', 'availability', 'product_code', 'image', 'created_at', 'updated_at', 'banner', 'adire', 'urban_wear', 'bags', )

class AdminMcategory(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',)}

class AdminCustomimg(admin.ModelAdmin):
    list_display = ('name', 'img',)

class AdminLoveit(admin.ModelAdmin):
    list_display = ( 'product', 'value',)


admin.site.register(Category, AdminCategory)
admin.site.register(PriceRange, AdminPriceRange)
admin.site.register(Brand, AdminBrand)
admin.site.register(Product, AdminProduct)
admin.site.register(Mcategory, AdminMcategory)
admin.site.register(Customimg, AdminCustomimg)
admin.site.register(Loveit, AdminLoveit)

