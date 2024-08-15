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
    permission_classes = [AllowAny]

    serializer_class = BrandSerializer

    def get_queryset(self):
        queryset = Brand.objects.all()
        brand_id = self.request.query_params.get('brand_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if brand_id:
            queryset = queryset.filter(id=brand_id)
        if category_id:
            queryset = queryset.filter(products__category_id=category_id).distinct()
        return queryset.order_by('name')



    def list(self,requst,*args,**kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset,many = True)
        data = {
            'data': serializer.data
        }
        return Response(data)

class ProductListView(generics.ListAPIView):
    permission_classes = [AllowAny]

    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        brand_id = self.request.query_params.get('brand_id', None)
        category_id = self.request.query_params.get('category_id', None)

        if brand_id:
            queryset = queryset.filter(brand_id=brand_id)
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset.order_by('name')

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = {
            'data': serializer.data
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