from django.urls import path

from api_v2.views import CategoryListView, BrandListView

urlpatterns = [
    path('categories', CategoryListView.as_view(), name = 'category_list'),
    path('brands', BrandListView.as_view(), name = 'brand_list'),
]