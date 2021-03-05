from rest_framework import serializers
from cart.models import OrderItem, Order
from shop_items.serializers import ShopItemSerializer


class OrderItemSerializers(serializers.ModelSerializer):
    order = serializers.StringRelatedField(read_only=True)
    product = ShopItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField(read_only=True)
    order = OrderItemSerializers(read_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'
