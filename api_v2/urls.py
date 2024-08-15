from django.urls import path

from api_v2.views import CategoryListView, BrandListView, ProductListView, OrderListView

urlpatterns = [
    path('categories', CategoryListView.as_view(), name = 'category_list'),
    path('brands', BrandListView.as_view(), name = 'brand_list'),
    path('products', ProductListView.as_view(), name = 'product_list'),
    path('order', OrderListView.as_view(), name = 'order_list')
]