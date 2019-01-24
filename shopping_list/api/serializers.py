from rest_framework import serializers
from shopping_list.models import Product


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name']
