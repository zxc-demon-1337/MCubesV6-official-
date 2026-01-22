from django.shortcuts import render

def choose_cube(request):
    return render(request, 'education/choose-cube.html')

def course_2x2_def_1(request):
    return render(request, 'education/course_2x2_def_1.html')