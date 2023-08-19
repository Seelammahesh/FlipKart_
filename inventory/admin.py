from django.contrib import admin
from .models import *
# Register your models here.



class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'product_id', 'product_quantity', 'product_stock', 'category']
    list_filter = ['category']
    search_fields = ['name','procuct_id']


class CategoryAdmin(admin.ModelAdmin):
    list_display =['category_name','category_type']
    #list_display =['category_name','category_type']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
