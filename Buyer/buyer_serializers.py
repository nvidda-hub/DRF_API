from rest_framework import serializers
from apiDev.models import Store, Product, Category, Customer, Order



class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'store_name', 'address']
