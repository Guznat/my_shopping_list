from django.urls import path
from .views import AddUserView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', AddUserView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    ]
# s
