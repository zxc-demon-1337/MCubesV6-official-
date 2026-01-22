from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_cube, name='education'),
    path('course_2x2_def_1', views.course_2x2_def_1, name='course_2x2_def_1')
]