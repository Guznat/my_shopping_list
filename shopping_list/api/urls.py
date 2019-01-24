from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ProductListAPIView.as_view(), name='api_list'),
    path('create/', views.ProductCreateAPIView.as_view(), name='api_create'),
]
