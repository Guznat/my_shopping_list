from rest_framework import generics
from .serializers import ProductModelSerializer
from shopping_list.models import Product


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self):
        return Product.objects.all()
