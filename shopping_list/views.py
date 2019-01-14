from django.shortcuts import render
from django.views import View
from .models import Product
# Create your views here.


class ShoppingListView(View):
    def get(self, request):
        products = Product.objects.all()
        ctx = {
            'products':products
        }
        return render(request, 'shopping_list/shipping_list.html', ctx)