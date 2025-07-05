from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny

from products.models import Orders, CustomUser
from products.serializers import OrdersSerializer, RegisterSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)  # доступно без аутентификации
    serializer_class = RegisterSerializer

