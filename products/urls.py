from django.urls import path
from .views import ProductList, ProductDetail

app_name = "products"

urlpatterns = [
    path('', ProductList.as_view(), name='list'),
    path('<slug:slug>/', ProductDetail.as_view(), name='detail'),
    path("category/<slug:slug>/", ProductList.as_view(), name="list_by_category")
]