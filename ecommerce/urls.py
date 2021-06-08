from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('produtos/', views.produtos, name='produtos'),
    path('produto_detalhe/<id>/', views.produto_detalhe, name='produto_detalhe'),
]