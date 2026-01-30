from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import MyAccountRegisterForm, MyAccountLoginForm
from django.contrib.auth import logout
import json
from django.http import JsonResponse
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = MyAccountRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            print("Avatar path:", user.avatar.name)
            login(request, user)
            return redirect('account:profile')
    else:
        form = MyAccountRegisterForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = MyAccountLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('account:profile')
            else:
                # Аутентификация не удалась
                messages.error(request, 'Неверный email или пароль')
        else:
            # Форма не валидна
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = MyAccountLoginForm()
    return render(request, 'account/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'account/profile.html')


def logout_view(request):
    logout(request)
    return redirect('account:login')

@login_required
def update_account(request):
    if request.method == 'POST':
        field = request.POST.get('field')
        user = request.user

        if field == 'nickname':
            nickname = request.POST.get('value')
            user.nickname = nickname
        elif field == 'email':
            email = request.POST.get('value')
            user.email = email
        elif field == 'password':
            password = request.POST.get('value')
            user.set_password(password)
        elif field == 'avatar':
            avatar = request.FILES.get('value')
            if avatar:
                user.avatar = avatar

        try:
            user.save()
            if field == 'password':
                from django.contrib.auth import update_session_auth_hash
                update_session_auth_hash(request, user)  # важно, чтобы юзер не вышел после смены пароля

            # Возвращаем новое значение
            new_value = getattr(user, field)
            if field == 'avatar':
                new_value = user.avatar.url if user.avatar else None

            return JsonResponse({'success': True, 'new_value': new_value})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

    return JsonResponse({'success': False, 'error': 'Invalid request'})