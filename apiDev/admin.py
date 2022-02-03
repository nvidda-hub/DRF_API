from django.contrib import admin
from apiDev.models import Article, Store, Product, Category, Customer, Order



admin.site.register(Article)

@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'store_name', 'address', 'store_link']

@admin.register(Product)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_mobile_num', 'customer_name', 'customer_address']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordered_at', 'product', 'customer']