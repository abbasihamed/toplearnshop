from django.urls import path
from shop_items.views import ShopItem

urlpatterns = [
    path('shopitems', ShopItem.as_view()),
]
