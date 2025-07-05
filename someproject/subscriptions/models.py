from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models


class Tariff(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    price = models.PositiveIntegerField(verbose_name='Цена')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'



class UserSubscription(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='subscription', blank=False,
                                null=False)
    tariff = models.ForeignKey('Tariff', on_delete=models.CASCADE, related_name='tariffs', blank=False, null=False)
    discount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Подписка {self.user}'
