from rest_framework import serializers
from shop_items.models import ShopItems


class ShopItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopItems
        fields = '__all__'
