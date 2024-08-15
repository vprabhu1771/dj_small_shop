from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.models import Category, Brand, Product, Order

from api_v2.serializers import CategorySerializer, BrandSerializer, ProductSerializer, OrderSerializer


# Create your views here.
class CategoryListView(generics.ListAPIView):
    permission_classes = [AllowAny]

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            "data": serializer.data
        }
        return Response(data)

class BrandListView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many= True)
        data = {
            "data" : serializer.data
        }
        return Response(data)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class =  ProductSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data ={
            "data" : serializer.data
        }
        return Response(data)

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class =  OrderSerializer
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data ={
            "data" : serializer.data
        }
        return Response(data)