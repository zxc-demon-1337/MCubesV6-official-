from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import MyAccount
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class MyAccountRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            # 'placeholder': _('Enter the password'),
            'autocomplete': 'new-password'
        }),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            # 'placeholder': _('Сonfirm the password'),
            'autocomplete': 'new-password'
        }),
    )

    class Meta:
        model = MyAccount
        fields = ('email', 'nickname', 'password1', 'password2', 'avatar')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                # 'placeholder': _('Email'),
                'autocomplete': 'email'
            }),
            'nickname': forms.TextInput(attrs={
                'class': 'form-control',
                # 'placeholder': _('Nickname'),
                'autocomplete': 'nickname'
            }),
            'avatar': forms.ClearableFileInput(attrs={
                'class': 'custom-file-input',
                'id': 'fileInput'
            })
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class MyAccountLoginForm(forms.Form):
    email = forms.EmailField(
    widget=forms.EmailInput(attrs={'autocomplete': 'username'})
)
    password = forms.CharField(
    widget=forms.PasswordInput(attrs={
        'autocomplete': 'current-password',
        'id': 'id_password'
    })
)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(email=email, password=password)
            if user is None:
                raise forms.ValidationError("Неверный email или пароль.")
            elif not user.is_active:
                raise forms.ValidationError("Аккаунт отключен.")
        return super().clean()