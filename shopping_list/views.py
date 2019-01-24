from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Product
from .forms import ListForm
from .api import serializers


def shopping_list(request):
    form = ListForm
    ctx = {'form': form}
    return render(request, 'shopping_list/shipping_list.html', ctx)


# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#
#         Product.objects.create(
#             name=name
#         )
#         return HttpResponse('')
#

def complete_product(request, id):
    product = Product.objects.get(pk=id)
    product.complete = True
    product.save()

    return redirect('index')


def checked_delete(request):
    Product.objects.filter(complete__exact=True).delete()

    return redirect('index')


def delete_all(request):
    Product.objects.all().delete()

    return redirect('index')
