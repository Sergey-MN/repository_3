from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from products.models import Orders, CustomUser
from products.serializers import OrdersSerializer, RegisterSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.none()
    serializer_class = OrdersSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Orders.objects.filter(customer_id=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

