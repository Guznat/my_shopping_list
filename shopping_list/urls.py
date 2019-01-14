from django.contrib import admin
from django.urls import path
from .views import ShoppingListView

urlpatterns = [
    path('', ShoppingListView.as_view(), name='shopping_list')
]