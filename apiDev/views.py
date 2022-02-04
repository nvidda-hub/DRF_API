from apiDev.models import Store, Product, Category, Customer, Order
from apiDev.serializers import StoreSerializer, ProductSerializer, CategorySerializer, CustomerSerializer, OrderSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import viewsets, status
from knox.auth import AuthToken



# user auth views
@api_view(['POST'])
def login_view(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']

    _, token = AuthToken.objects.create(user)

    return Response({
        'user_info':
        {
            'id':user.id, 
            'username':user.username, 
        }, 
        'token':token
    })


@api_view(["GET"])
def get_user_data(request):
    user = request.user

    if user.is_authenticated:
        return Response({
            'user_info':{
                "id":"user.id",
                "username":user.username,
            },

        })
    
    return Response({'error':'You are not authorize to access this end point'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)

    user = serializer.save()

    _, token = AuthToken.objects.create(user)

    return Response({
                        'user_info':
                        {
                            'id':user.id, 
                            'username':user.username, 
                        }, 
                        'token':token
                    })

    

class StoreViewSet(viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()
    

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

