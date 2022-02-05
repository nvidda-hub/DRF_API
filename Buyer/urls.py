from django.urls import path, include
from Buyer import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

urlpatterns = [
    path('', router.get_api_root_view()),
    path('stores/<slug:link>/', views.StoreDetailView.as_view()),

]