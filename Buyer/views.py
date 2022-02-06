from rest_framework.response import Response 
from rest_framework.views import APIView 
from apiDev.models import Store, Product
from Buyer.buyer_serializers import ProductCatalogSerializer, StoreDetailSerializer
from apiDev.serializers import ProductSerializer



class StoreDetailView(APIView):     
    def get(self, request, link): 
        store = list(Store.objects.filter(store_link=link).values())
        store_serializer = StoreDetailSerializer(store) 
        return Response(store)



class ProductCatalogAndCategoryView(APIView):
    query_set = Product.objects.all()
    serializer_class = ProductCatalogSerializer     
    def get(self, request, link): 
        get_store = Store.objects.get(store_link=link)
        products = Product.objects.filter(store_name=get_store).values()
        product_serializer = ProductCatalogSerializer(products) 
        return Response(products)         