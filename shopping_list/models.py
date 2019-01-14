from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=52)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    clicked = models.BooleanField(default=False)

    def __str__(self):
        return f"Product: {self.name}"



    # def get_absolute_url(self):
    #     return reverse("niewiem", kwargs={"id": self.id})


class Profile(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
