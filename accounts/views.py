from django.contrib.auth import login
from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.models import User
from .forms import CreateUserForm



class AddUserView(View):
    def get(self, request):
        form = CreateUserForm()
        ctx = {
            'form': form
        }
        return render(request, 'registration/signup.html', ctx)

    def post(self, request):
        form = CreateUserForm(request.POST)
        ctx = {
            'form': form
        }
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['login'],
                password=form.cleaned_data['password'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            login(request, user)
            return redirect(reverse('index'))
        return render(request, 'registration/signup.html', ctx)
    # s
