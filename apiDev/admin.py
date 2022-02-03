from django.contrib import admin
from apiDev.models import Article, Store
# Register your models here.

admin.site.register(Article)
@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'store_name', 'address', 'store_link']