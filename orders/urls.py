from django.urls import path
from django.urls.resolvers import URLPattern

from .views import OrderCreateView

app_name = 'orders'

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create'),
]