from django.contrib import admin
from apiDev.models import Store, Product, Category, Customer, Order



@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'store_name', 'address', 'store_link', 'owner']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'description', 'MRP', 'sale_price', 'category', 'store', 'image']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_email', 'customer_name', 'customer_address']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordered_at', 'product', 'customer']