from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from cart.models import OrderItem, Order
from shop_items.models import ShopItems
from cart.serializers import OrderSerializer, OrderItemSerializers


# Create your views here.
# ایجاد سب خرید
class SetOrder(APIView):
    def get(self, request):
        print(request.user)
        query = Order.objects.filter(owner=request.user)
        serializer = OrderSerializer(query, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        data = True
        query = Order.objects.filter(owner=request.user)
        for q in query:
            data = q.is_payed
        if data:
            serializer = OrderSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save(owner=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data={'status': 'You have one'}, status=status.HTTP_400_BAD_REQUEST)


# اضافه کردن ایتم به سبد خرید
class OrderList(APIView):
    def get(self, request):
        query = OrderItem.objects.all()
        serializer = OrderItemSerializers(query, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        # سریالایز کردن
        serializer = OrderItemSerializers(data=request.data, context={'request': request})
        # گرفتن نام کاربر و اسم محصول از درخواست ارسال شده
        order = request.user
        product = request.data.get('product')
        # در اوردن مدل محصول مورد نظر
        items = ShopItems.objects.get(title=product)
        user = Order.objects.get(owner=order, is_payed=False)
        # چک کردن برای این که محصول قبلا ایجاد نشده باشد
        query = OrderItem.objects.filter(product__title=product)
        if not query:
            if serializer.is_valid():
                serializer.save(order=user, product=items)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response({'status': 'Not valid'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Items already available'}, status=status.HTTP_400_BAD_REQUEST)
