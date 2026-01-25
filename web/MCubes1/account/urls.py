from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_acc, name='account'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),



]