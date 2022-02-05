from rest_framework import serializers
from apiDev.models import Store, Product, Category, Customer, Order



class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address']

class ProductCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'MRP', 'sale_price', 'category', 'image']
