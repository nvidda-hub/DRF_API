from django.urls import path, include
from apiDev import views
from rest_framework.routers import DefaultRouter


app_name = 'apiDev'

router = DefaultRouter()

router.register('article', views.ArticleViewSet, basename="article")
router.register('store', views.StoreViewSet, basename="store")

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
]
