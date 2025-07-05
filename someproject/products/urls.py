from django.urls import path, include
from rest_framework import routers

from products.views import OrdersViewSet

router = routers.SimpleRouter()
router.register(r'products', OrdersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]