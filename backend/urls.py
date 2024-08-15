from django.urls import path
from .views import ViewPDF

urlpatterns = [
    path('invoice/<str:order_id>', ViewPDF.as_view())
]