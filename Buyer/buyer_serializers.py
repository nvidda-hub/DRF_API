from rest_framework import serializers
from apiDev.models import Store, Product, Category, Customer, Order
from Buyer.models import Cart
from apiDev.serializers import ProductSerializer, StoreSerializer



class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address']

class ProductCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'MRP', 'sale_price', 'category', 'image']


class CartSerializers(serializers.ModelSerializer):
    products = ProductSerializer(read_only=True, many=True)
    store = StoreSerializer(read_only=True, many=True)
    class Meta:
        model = Cart
        fields = ['cart_id', 'created_at', 'products', 'store']
