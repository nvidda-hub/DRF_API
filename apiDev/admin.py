from django.contrib import admin
from apiDev.models import Store, Product, Category, Customer, Order, Account



@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'date_joined', 'is_staff', 'is_active']

@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'store_name', 'address', 'store_link', 'owner']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'description', 'MRP', 'sale_price', 'qty', 'category', 'store_name', 'image']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_email', 'customer_name', 'customer_address']

@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'ordered_at', 'product', 'customer']