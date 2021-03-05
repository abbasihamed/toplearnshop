from django.urls import path
from cart.views import *

urlpatterns = [
    path('order/', OrderList.as_view()),
    path('setorder/', SetOrder.as_view()),
]
