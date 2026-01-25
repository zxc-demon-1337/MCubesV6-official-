from django.shortcuts import render

def choose_cube(request):
    return render(request, 'education/choose-cube.html')

def course_2x2_def_1(request):
    return render(request, 'education/course_2x2_def_1.html')

def course_2x2_def_2(request):
    return render(request, 'education/course_2x2_def_2.html')

def course_2x2_def_3(request):
    return render(request, 'education/course_2x2_def_3.html')

def course_2x2_def_4(request):
    return render(request, 'education/course_2x2_def_4.html')

def course_2x2_def_5(request):
    return render(request, 'education/course_2x2_def_5.html')