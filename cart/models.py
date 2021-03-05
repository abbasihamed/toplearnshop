from django.contrib.auth.models import User
from django.db import models

from shop_items.models import ShopItems


class Order(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    is_payed = models.BooleanField(default=False)

    def __str__(self):
        return self.owner.username


class OrderItem(models.Model):
    product = models.ForeignKey(ShopItems, on_delete=models.CASCADE, related_name='product')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order')
    date_created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()
