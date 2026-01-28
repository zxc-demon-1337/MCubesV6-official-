from django.contrib import admin
from .models import MyAccount
# Register your models here.

@admin.register(MyAccount)
class YourAccountModelAdmin(admin.ModelAdmin):
    list_display = ['nickname', 'email',  'date_joined', 'avatar']