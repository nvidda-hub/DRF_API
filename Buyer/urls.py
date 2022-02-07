from django.urls import path, include
from Buyer import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('', router.get_api_root_view()),
    path('stores/<slug:link>/', views.StoreDetailView.as_view()),
    path('product_catalog_and_categories/<slug:link>/', views.ProductCatalogAndCategoryView.as_view()),
    path('carts/', views.ListCartView.as_view(), name="carts"),
    path('carts/<int:pk/', views.CartDetialView.as_view(), name="cartDetaiil")


]