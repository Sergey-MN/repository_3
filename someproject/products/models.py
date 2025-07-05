import requests
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

phone_validator = RegexValidator(
    regex=r'^\+7\d{10}$',
    message="Номер должен быть в формате: '+7XXXXXXXXXX'."
)


class MyManager(models.Manager):
    def create(self, *args, **kwargs):
        instance = super().create(*args, **kwargs)
        try:
            response = requests.get(
                f"https://api.telegram.org/bot7529171556:AAFrrFzxO5MBPqaGOrfqdAiya8nKbhBnKT4/sendMessage?chat_id={instance.customer.telegram_id}&text=Вам пришёл новый заказ!")
        except Exception as e:
            print(f'Error: {e}')
        return instance

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, validators=[phone_validator], verbose_name='Телефон', unique=True)
    telegram_id = models.CharField(max_length=20, blank=True, null=True)


class Orders(models.Model):
    customer = models.ForeignKey(get_user_model(), related_name='customer', on_delete=models.CASCADE, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    products = models.JSONField(default=dict)

    objects = MyManager()