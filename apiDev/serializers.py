from rest_framework import serializers
from apiDev.models import Store, Product, Category, Customer, Order
from django.contrib.auth.models import User



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {
            "password":{"write_only":True},
        }
    
    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        user = User.objects.create(username=username, password=password)

        return user


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address', 'store_link', 'owner']
        extra_kwargs = {
            'store_link': {'read_only': True},
        }

class ProductSerializer(serializers.ModelSerializer):
    # category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'MRP', 'sale_price', 'category', 'store']
        extra_kwargs = {
            'id': {'read_only': True},
        }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class GroupSerializer(serializers.ModelSerializer):
    # category = serializers.CharField()

    class Meta:
        model = Product
        fields = ['id', 'category']
        extra_kwargs = {
            'id': {'read_only': True},
        }


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'customer_email', 'customer_address']


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'ordered_at', 'product', 'customer']
        