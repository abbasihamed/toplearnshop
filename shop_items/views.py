from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from shop_items.models import ShopItems
from shop_items.serializers import ShopItemSerializer


class ShopItem(APIView):
    def get(self, request):
        query = ShopItems.objects.all()
        serializer = ShopItemSerializer(query, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
