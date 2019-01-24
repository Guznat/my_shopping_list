from django.urls import path

from . import views

urlpatterns = [
    path('', views.shopping_list, name='index'),
    # path('add/', views.add_product, name='add'),
    path('complete/<id>', views.complete_product, name='complete'),
    path('deletecomplete', views.checked_delete, name='deletecomplete'),
    path('deleteall', views.delete_all, name='deleteall')
]
