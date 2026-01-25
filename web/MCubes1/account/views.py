from django.shortcuts import render

# Create your views here.
def my_acc(request):
    return render(request, 'account/my_acc.html')

def register(request):
    return render(request, 'account/register.html')

def login(request):
    return render(request, 'account/login.html')