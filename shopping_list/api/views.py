from rest_framework import generics
from django.db.models import Q
from .serializers import ProductModelSerializer, ProductUpdateSerializer
from shopping_list.models import Product
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response


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


class CompleteProductAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductUpdateSerializer
    permission_classes = (permissions.AllowAny,)
