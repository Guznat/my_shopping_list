from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=180)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name