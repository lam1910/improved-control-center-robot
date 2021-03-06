from django.shortcuts import render
from rest_framework import generics

from .models import Order
from .serializers import OrderSerializer


# Create your views here.
class ListOrder(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DetailOrder(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer