from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from subscriptions.models import Tariff, UserSubscription

from subscriptions.serializers import TariffSerializer, SubscriptionSerializer


class TariffAPIView(ListAPIView):
    queryset = Tariff.objects.all()
    serializer_class = TariffSerializer


class SubscriptionPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = UserSubscription.objects.all()
    serializer_class = SubscriptionSerializer
    pagination_class = SubscriptionPagination
