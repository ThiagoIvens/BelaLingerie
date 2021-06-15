from django.contrib import admin
from django.urls import path
from . import views

app_name = "ecommerce"

urlpatterns = [
    path('', views.home, name='home'),
    path('sobre/', views.about, name='about'),
]