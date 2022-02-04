from django.urls import path, include
from apiDev import views
from rest_framework.routers import DefaultRouter
from knox import views as knox_views


app_name = 'apiDev'

router = DefaultRouter()

router.register('store', views.StoreViewSet, basename="store")
router.register('product', views.ProductViewSet, basename="product")
router.register('category', views.CategoryViewSet, basename="category")
router.register('customer', views.CustomerViewSet, basename="customer")
router.register('order', views.OrderViewSet, basename="order")

urlpatterns = [
    path('', router.get_api_root_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    path('user/login/', views.login_view),
    path('register/', views.register_user),
    path('getuser/', views.get_user_data),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
]
