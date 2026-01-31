from django.urls import path
from . import views

app_name = 'rubik_timer'

urlpatterns = [
    path('', views.timer_view, name='timer'),
]