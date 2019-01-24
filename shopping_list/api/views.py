from rest_framework import generics
from django.db.models import Q
from .serializers import ProductModelSerializer
from shopping_list.models import Product


class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductModelSerializer

    def get_queryset(self, *args, **kwargs):
        qs = Product.objects.all()
        query = self.request.GET.get('q', None)
        if query is not None:
            qs = qs.filter(
                Q(name__icontains=query)
            )
        return qs


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductModelSerializer
