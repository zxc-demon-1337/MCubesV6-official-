from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose_cube, name='education'),
    path('course_2x2_def_1', views.course_2x2_def_1, name='course_2x2_def_1'),
    path('course_2x2_def_2', views.course_2x2_def_2, name='course_2x2_def_2'),
    path('course_2x2_def_3', views.course_2x2_def_3, name='course_2x2_def_3'),
    path('course_2x2_def_4', views.course_2x2_def_4, name='course_2x2_def_4'),
    path('course_2x2_def_5', views.course_2x2_def_5, name='course_2x2_def_5'),

]