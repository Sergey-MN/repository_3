from django.urls import path, include
from rest_framework import routers

from subscriptions.views import TariffAPIView, SubscriptionViewSet

router = routers.SimpleRouter()
router.register(r'subscriptions', SubscriptionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('tariffs/', TariffAPIView.as_view()),
]
