from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from .models import Product
from .forms import ListForm
from django.views.generic import RedirectView
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

# class ProductCompliteRedirect(RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         id_ = self.kwargs.get("id")
#         print(id_)
#         obj = get_object_or_404(Product, pk=id_)
#         return obj.get_absolute_url()
