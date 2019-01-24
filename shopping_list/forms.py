from django import forms
from .models import Product


class ListForm(forms.ModelForm):
    name = forms.CharField(max_length=180,
                           widget=forms.TextInput)

    class Meta:
        model = Product
        fields = ['name', ]
