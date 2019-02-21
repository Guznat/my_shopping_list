import django.forms as forms
from django.contrib.auth.models import User

class CreateUserForm(forms.Form):
    login = forms.CharField(max_length=24)
    password = forms.CharField(max_length=48, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=48, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=24)
    last_name = forms.CharField(max_length=24)
    email = forms.EmailField(max_length=24, widget=forms.EmailInput)

    def clean(self):
        data = self.cleaned_data
        if data['password'] != data['confirm_password']:
            raise forms.ValidationError('Password is not the same.')
        if User.objects.filter(username=data['login']):  # s
            raise forms.ValidationError('User already exist.')
        return data