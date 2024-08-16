from django.urls import path

from api_v2.views import CategoryListView, BrandListView, ProductListView, OrderListView, CartView, CartItemView, \
    ClearCartView, UserCreateAPIView, CustomAuthToken

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

    path('register', UserCreateAPIView.as_view(), name='create'),

    # Login Type 1
    path('token', obtain_auth_token, name='api_token_auth'),

    # Login Type 2
    path('login', CustomAuthToken.as_view(), name='custom_api_token_auth'),

    path('categories', CategoryListView.as_view(), name = 'category_list'),
    path('brands', BrandListView.as_view(), name = 'brand_list'),
    path('products', ProductListView.as_view(), name = 'product_list'),


    path('cart/', CartView.as_view(), name='cart'),
    path('cart/item/', CartItemView.as_view(), name='cart-item'),
    path('clear-cart', ClearCartView.as_view(), name='clear-cart'),

    path('order', OrderListView.as_view(), name = 'order_list')
]