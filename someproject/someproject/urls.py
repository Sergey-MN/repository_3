from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from products.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('subscriptions.urls')),
    path('api/', include('products.urls')),
    path('api/auth/', include('rest_framework.urls')),
    path('api/register/',  RegisterView.as_view()),
]
