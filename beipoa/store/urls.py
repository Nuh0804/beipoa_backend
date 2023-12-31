from django.urls import path
from django.urls.conf import include
from rest_framework_nested import routers
from . import views

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')

products_router = routers.NestedDefaultRouter(
    router, 'products', lookup='product')
products_router.register('images', views.ProductImageViewSet, basename='product-images')


# URLConf
urlpatterns = router.urls + products_router.urls