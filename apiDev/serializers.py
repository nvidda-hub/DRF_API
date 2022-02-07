from rest_framework import serializers
from apiDev.models import Store, Product, Category, Customer, Order
from apiDev.models import Account



class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['username', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def save(self):
        account = Account(
            username=self.validated_data['username']
        )
        password = self.validated_data['password']

        account.set_password(password)
        account.save()
        return account


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address', 'store_link', 'owner']
        extra_kwargs = {
            'store_link': {'read_only': True},
        }


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'MRP', 'sale_price', 'category', 'qty', 'store_name', 'image']
        extra_kwargs = {
            'id': {'read_only': True},
        }

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['store_name'] = StoreSerializer(instance.store_name).data
        rep['category'] = CategorySerializer(instance.category).data
        return rep

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']



class CustomerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=30, min_length=8)
    class Meta:
        model = Customer
        fields = ['customer_name', 'customer_email','customer_address','password']
        extra_kwargs = {
            'password': {'read_only': True},
        }

    def save(self):
        customer_account = Customer(
            customer_name=self.validated_data['customer_name'],
            customer_email=self.validated_data['customer_email'],
            customer_address=self.validated_data['customer_address'],
        )
        password = self.validated_data['password']

        customer_account.set_password(password)
        customer_account.save()
        customer_account.is_staff = False
        return customer_account


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'ordered_at', 'product', 'customer']
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['store_name'] = ProductSerializer(instance.product).data
        rep['customer'] = CustomerSerializer(instance.customer).data
        return rep